from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewsets


router = DefaultRouter()
router.register('', CommentViewsets)

urlpatterns = [
    path('', include(router.urls)),
]
