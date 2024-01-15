from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewsets


router = DefaultRouter()
router.register('', CategoryViewsets)

urlpatterns = [
    path('', include(router.urls))
]
