from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSets


router = DefaultRouter()
router.register('', PostViewSets)


urlpatterns = [
    path('', include(router.urls)),
]

