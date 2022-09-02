from django.shortcuts import render
from .serializers import CategorySerializer
from rest_framework.generics import ListAPIView
from onlinestore.models import Category


class CategoryList(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

