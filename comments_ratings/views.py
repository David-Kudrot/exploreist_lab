from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CommentSerializer
from .models import CommentModel
# Create your views here.

class CommentViewsets(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
