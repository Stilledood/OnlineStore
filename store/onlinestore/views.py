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


class ProductList(View):
    '''Class to contsruct a view using pagination to display a list of Product objects'''

    model = Product
    template_name = 'onlinestore/product_list.html'
    paginated_by = 10
    page_kwargs = 'page'

    def get(self, request):
        product_list = self.model.objects.all()
        paginator = Paginator(product_list, self.page_kwargs)
        page_number = request.GET.get(self.page_kwargs)

        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        if page.has_previous():
            previous_page_url = "?{pkw}={n}".format(pkw=self.page_kwargs, n=page.previous_page_number())
        else:
            previous_page_url = None

        if page.has_next():
            next_page_url = "?{pkw}={n}".format(pkw=self.page_kwargs, n=page.next_page_number())
        else:
            next_page_url = None

        context = {
            'has_other_page': page.has_other_pages(),
            'paginator': paginator,
            'previous_page': previous_page_url,
            'next_page': next_page_url,
            'product_list': page
        }

        return render(request, self.template_name, context=context)


class ProductDetails(View):
    '''Class to construct a view ti display details for a product object'''

    model=Product
    template_name='onlinestore/product_details.html'

    def get(self,request,pk):
        product=get_object_or_404(self.model,pk=pk)
        context={'product':product}
        return render(request,self.template_name,context=context)







