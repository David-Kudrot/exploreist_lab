from rest_framework import serializers

from django.contrib.auth.models import User
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'



class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    phone_no=serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'phone_no']
        
        
    def save(self):
        username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email=self.validated_data['email']
        password=self.validated_data['password']
        password2=self.validated_data['confirm_password']
        phone_no=self.validated_data['phone_no']
        
        if password != password2:
            raise serializers.ValidationError({'error':"Password doesn't match!"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email already exists"})
        
        account = User(username=username, email=email, first_name=first_name, last_name=last_name)#password k set_password() function die set kora lagbe
        account.set_password(password)
        account.is_active = False
        account.save()
        return account
    
    
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)