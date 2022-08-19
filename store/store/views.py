from onlinestore.models import Category,Product
from blog.models import Post
from django.views.generic import View
from django.shortcuts import redirect,render
from shoppingcart.models import Order
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

class GeneralView(View):
    '''Class to create a view for first page of the website'''
    template_name='base.html'

    def get(self,request):
        category_short_list=Category.objects.all()
        new_arrivals=Product.objects.all()[:8]
        featured_products=Product.objects.filter(featured=True)
        latest_blog=Post.objects.all()[:3]
        banner_item1=featured_products[0]
        banner_item2=featured_products[1]
        banner_item3=featured_products[2]
        user=request.user
        order=[]
        if user.is_authenticated:
            order=get_object_or_404(Order,user=request.user)
        cart_items=[]
        try:
            cart_items=order.orderitem_set.all()
        except:
            pass



        context={
            'category_list':category_short_list,
            'new_arrivals':new_arrivals,
            'featured_products':featured_products,
            'latest_blogs':latest_blog,
            'banner_item1':banner_item1,
            'banner_item2':banner_item2,
            'banner_item3':banner_item3,
            'cart_items':cart_items,
            'order':order

        }

        return render(request,self.template_name,context=context)


