from rest_framework import serializers
from onlinestore.models import Product,Category
from blog.models import Post


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    '''Class to create a model serializer for Category objects'''

    product_set=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='product-detail')

    class Meta:
        model=Category
        fields=('url','name','image','product_set')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    '''Class to create a model serializer for Product objects'''
    post_set=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='post-detail')


    class Meta:
        model=Product
        fields=('url','name','description','date_added','dimensions','weight','post_set')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    '''Class to create a model serializer for Post objects'''

    products=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='product-detail')

    class Meta:
        model=Post
        fields=('url','title','date_added','products')

