from django.shortcuts import render
from .serializers import CategorySerializer,ProductSerializer,PostSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from onlinestore.models import Category,Product
from blog.models import Post
from rest_framework import filters
from django_filters import rest_framework as filters
from .custompermision import CustomPermission
from rest_framework import permissions
from rest_framework.throttling import ScopedRateThrottle


class CategoryList(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ('^name',)
    filter_fields = ('name',)
    ordering_fields = ('name',)
    permission_classes = (permissions.IsAuthenticated,)


class CategoryDetails(RetrieveAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

class CustomProductFilter(filters.FilterSet):
    '''Class to construcyt a personalized filter to sort product by date added '''

    from_date_added = filters.DateFilter(field_name='date_added',lookup_expr='gte')
    until_date_added = filters.DateFilter(field_name='date_added',lookup_expr='lte')


    class Meta:
        model = Product
        fields=(
            'date_added',
            'from_date_added',
            'until_date_added'

        )




class ProductList(ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class=CustomProductFilter
    search_fields = ('^name',)
    filter_fields = ('name','date_added')
    ordering_fields = ('name','date_added')
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = (ScopedRateThrottle,)
    throttle_scope = 'products'



class ProductDetails(RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = (ScopedRateThrottle,)
    throttle_scope = 'products'

class PostList(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_fields = ('name','date_added',)
    search_fields = ('^name',)
    ordering_fields = ('name','date_added')
    permission_classes = (permissions.IsAuthenticated,)

class PostDetails(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (CustomPermission,permissions.IsAuthenticatedOrReadOnly)


