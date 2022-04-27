from django.contrib import admin
from .models import Product,Category,Tag
from django.db.models import Count


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Class to create a custom admin product view'''
    list_display=('name','date_added','price','tags_number')
    list_filter = ('name','price')
    date_hierarchy = 'date_added'
    search_fields = ('name','price','date_added')

    fieldsets = (
        ('Principal',{
            'fields':('name','price','description','dimensions','weight','image','featured','reduced_price','new_price')
        }),
        ('Related',{
            'fields':('category','tags')
        })
    )
    filter_horizontal = ('tags',)

    def get_queryset(self, request):
        queryset=super().get_queryset(request)
        return queryset.annotate(tag_number=Count('tags'))

    def tags_number(self,product):
        return product.tags.count()
    tags_number.short_description='Number of tags'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Class to construct a custom admin category view'''
    list_display=('name','slug','product_number')
    list_filter = ('slug',)
    search_fields = ('slug',)
    fieldsets = (
        ('Principal',{
            'fields':('name','slug',)
        }),
    )

    def get_queryset(self, request):
        queryset=super().get_queryset(request)
        return queryset.annotate(products_number=Count('product'))

    def product_number(self,category):
        return category.product_set.count()
    product_number.short_description='Number of Products'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    '''Class to construct a custom admin tag view'''

    list_display = ('name','slug','product_number',)
    list_filter = ('slug',)
    search_fields = ('slug','name',)

    fieldsets = (
        ('Principal',{
            'fields':('name','slug')
        }),
    )

    def get_queryset(self, request):
        queryset=super().get_queryset(request)
        return queryset.annotate(product_count=Count('product'))

    def product_number(self,tag):
        return tag.product_set.count()

    product_number.short_description='Number of products'
