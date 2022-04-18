from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,Product,Tag
from django.views.generic import View


class CategoryList(View):
    '''Class to construct a view to list all the category objects from out database'''

    model=Category
    template_name='onlinestore/category_list.html'

    def get(self,request):
        category_list=self.model.objects.all()
        context={'category_list':category_list}
        return render(request,self.template_name,context=context)


class CategoryDetails(View):
    '''Class to display all the details of a Category object'''

    model=Category
    template_name='onlinestore/category_details.html'

    def get(self,request,slug):
        category=get_object_or_404(self.model,slug__iexact=slug)
        context={'category':category}
        return render(request,self.template_name,context=context)







