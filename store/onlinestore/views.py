from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,Product,Tag
from django.views.generic import View
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


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


class TagList(View):
    '''Class to display a list of all Tag Objects'''

    model=Tag
    template_name='onlinestore/tag_list.html'

    def get(self,request):
        tag_list=self.model.objects.all()
        context={'tag_list':tag_list}
        return render(request,self.template_name,context=context)

class TagDetails(View):
    '''Class to display all the details for a Tag object'''

    model=Tag
    template_name='onlinestore/tag_details.html'

    def get(self,request,slug):
        tag=get_object_or_404(self.model,slug__iexact=slug)
        context={'tag':tag}
        return render(request,self.template_name,context=context)








