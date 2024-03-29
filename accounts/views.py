from django.shortcuts import render, redirect
from django.views import View
from .serializers import UserLoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UserRegisterSerializer, UserSerializer
from  .models import UserModel
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer




class UserRegistrationAPIView(APIView):
    serializer_class = UserRegisterSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)
            confirm_link = f"http://127.0.0.1:8000/accounts/active/{uid}/{token}"
            
            
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Wow, well done!")
        return Response(serializer.errors)
    
    
    
#account activation
class ActivateAccount(View):
    def get(self, request, uid64, token):
        try:
            uid = urlsafe_base64_decode(uid64).decode()
            user = User._default_manager.get(pk=uid)
        except User.DoesNotExist:
            user = None 

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            return redirect('register')
        
        
        


class UserLoginAPIView(APIView):
    def post(self, request):  # jehetu login korte form post kora lage tai only post use korlam
        serializer = UserLoginSerializer(data=self.request.data) # same to same jemon form = forms.UserLoginForm(user=self.request.user) kortam
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            
            user = authenticate(username=username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)# token = token thakbe or  _ = toaken create hobe
                print(token)
                print(_)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid Credentials!'})
        return Response(serializer.errors)