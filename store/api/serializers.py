from rest_framework import serializers
from onlinestore.models import Product,Category
from blog.models import Post


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    '''Class to create a model serializer for Category objects'''

    products=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='product_detail')

    class Meta:
        model=Category
        fields=('url','name','image','products')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    '''Class to create a model serializer for Product objects'''

