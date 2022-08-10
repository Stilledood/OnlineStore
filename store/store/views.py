from onlinestore.models import Category,Product
from blog.models import Post
from django.views.generic import View
from django.shortcuts import redirect,render


class GeneralView(View):
    '''Class to create a view for first page of the website'''
    template_name='general_view.html'

    def get(self,request):
        category_short_list=Category.objects.all()
        new_arrivals=Product.objects.all()[:8]
        featured_products=Product.objects.filter(featured=True)
        latest_blog=Post.objects.all()[:3]
        banner_item1=featured_products[0]
        banner_item2=featured_products[1]
        banner_item3=featured_products[2]

        context={
            'category_list':category_short_list,
            'new_arrivals':new_arrivals,
            'featured_products':featured_products,
            'leatest_blog':latest_blog,
            'banner_item1':banner_item1,
            'banner_item2':banner_item2,
            'banner_item3':banner_item3,

        }

        return render(request,self.template_name,context=context)


