from django.shortcuts import render
from .serializers import CategorySerializer,ProductSerializer,PostSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from onlinestore.models import Category,Product
from blog.models import Post


class CategoryList(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ('^name',)
    filter_fields = ('name',)
    ordering_fields = ('name',)


class CategoryDetails(RetrieveAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ('^name',)
    filter_fields = ('name','date_added')
    ordering_fields = ('name','date_added')


class ProductDetails(RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PostList(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_fields = ('name','date_added',)
    search_fields = ('^name',)
    ordering_fields = ('name','date_added')

class PostDetails(RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


