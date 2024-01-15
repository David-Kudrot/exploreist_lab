from django.urls import path
from .views import UserRegistrationAPIView, ActivateAccount, UserLoginAPIView



urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('active/<str:uid64>/<str:token>', ActivateAccount.as_view(), name='activate_account'), # class based activation
    path('login/', UserLoginAPIView.as_view(), name='login'),

]
