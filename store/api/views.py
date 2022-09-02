from django.shortcuts import render
from .serializers import CategorySerializer,ProductSerializer,PostSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from onlinestore.models import Category,Product
from blog.models import Post


class CategoryList(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetails(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetails(RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PostList(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetails(RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


