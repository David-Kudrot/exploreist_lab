from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivateAccount, UserLoginAPIView, UserRegistrationAPIView, UserViewSet



router = DefaultRouter()
router.register('list', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('active/<str:uid64>/<str:token>', ActivateAccount.as_view(), name='activate_account'), # class based activation
    path('login/', UserLoginAPIView.as_view(), name='login'),

]
