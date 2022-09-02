from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,Product,Tag,Review
from django.views.generic import View
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import CategoryForm,TagForm,ProductForm,ReviewForm
from user.decorators import custom_login_required,custom_permission_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from shoppingcart.forms import AddToCartForm
from shoppingcart.models import Order,OrderItem
import random




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
        products=category.product_set.all()
        banner_product=random.choice(products)

        context={'category':category,'product_list':products,'banner_product':banner_product}
        return render(request,self.template_name,context=context)

@custom_permission_required('onlinestore.add_category')
class CategoryAdd(View):
    '''Class to construct a view to add Category objects'''


    template_name='onlinestore/category_add.html'
    form_class=CategoryForm

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class()})

    def post(self,request):
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            new_category=bound_form.save()
            return redirect(new_category.get_absolute_url())
        else:
            return render(request,self.template_name,{'form':bound_form})



@custom_permission_required('onlinestore.change_category')
class CategoryChange(View):
    '''Class to construct a view to change Category objects'''

    model=Category
    template_name='onlinestore/category_change.html'
    form_class=CategoryForm

    def get(self,request,slug):
        category_obj=get_object_or_404(self.model,slug__iexact=slug)
        return render(request,self.template_name,{'form':self.form_class(instance=category_obj),'category':category_obj})

    def post(self,request,slug):
        category_obj=get_object_or_404(self.model,slug__iexact=slug)
        bound_form=self.form_class(request.POST,instance=category_obj)
        if bound_form.is_valid():
            updated_category=bound_form.save()
            return redirect(updated_category.get_absolute_url())
        else:
            return render(request,self.template_name,{'form':bound_form,'category':category_obj})



@custom_permission_required('onlinestore.delete_category')
class CategoryDelete(View):
    '''Class to construct a view to delete Category objects'''

    model=Category
    template_name='onlinestore/category_delete.html'

    def get(self,request,slug):
        category=get_object_or_404(self.model,slug__iexact=slug)
        return render(request,self.template_name,{'category':category})

    def post(self,request,slug):
        category=get_object_or_404(self.model,slug__iexact=slug)
        category.delete()
        return redirect('category_list')
    




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



@custom_permission_required('onlinestore.add_tag')
class TagAdd(View):
    '''Class to create a view to add Tag objects'''

    model=Tag
    template_name='onlinestore/tag_add.html'
    form_class=TagForm

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class()})

    def post(self,request):
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag=bound_form.save()
            return redirect(new_tag.get_absolute_url())
        else:
            return render(request,self.template_name,{'form':bound_form})



@custom_permission_required('onlinestore.change_tag')
class TagUpdate(View):
    '''Class to construct a view to change Tag objects'''

    model=Tag
    template_name='onlinestore/tag_update.html'
    form_class=TagForm

    def get(self,request,slug):
        tag=get_object_or_404(self.model,slug__iexact=slug)
        return  render(request,self.template_name,{'form':self.form_class(instance=tag),'tag':tag})

    def post(self,request,slug):
        tag=get_object_or_404(self.model,slug__iexact=slug)
        bound_form=self.form_class(request.POST,instance=tag)
        if bound_form.is_valid():
            updated_tag=bound_form.save()
            return redirect(updated_tag.get_absolute_url())
        else:
            return render(request,self.template_name,{'form':bound_form,'tag':tag})



@custom_permission_required('onlinestore.delete_tag')
class TagDelete(View):
    '''Class to create a view to delete a tag object'''

    model=Tag
    template_name='onlinestore/tag_delete.html'

    def get(self,request,slug):
        tag=get_object_or_404(self.model,slug__iexact=slug)
        return render(request,self.template_name,{'tag':tag})

    def post(self,request,slug):
        tag=get_object_or_404(self.model,slug__iexact=slug)
        tag.delete()
        return redirect('tag_list')





class ProductList(View):
    '''Class to contsruct a view using pagination to display a list of Product objects'''

    model = Product
    template_name = 'onlinestore/product_list.html'
    paginated_by = 12
    page_kwargs = 'page'

    def get(self, request):
        product_list = self.model.objects.all()
        paginator = Paginator(product_list, self.paginated_by)
        page_number = request.GET.get(self.page_kwargs)
        banner_product=random.choice(product_list)

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
            'product_list': page,
            'banner_product':banner_product
        }

        return render(request, self.template_name, context=context)



class ProductDetails(View):
    '''Class to construct a view ti display details for a product object'''

    model=Product
    template_name='onlinestore/product_details.html'
    form_class=AddToCartForm


    def get(self,request,pk):
        product=get_object_or_404(self.model,pk=pk)
        context={'product':product,
                 'form':self.form_class()}

        return render(request,self.template_name,context=context)



    @method_decorator(login_required)
    def post(self,request,pk):
        product=get_object_or_404(self.model,pk=pk)
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            user = request.user
            order, created = Order.objects.get_or_create(user=user, complete=False)
            print(order.orderitem_set.all())


            if len(OrderItem.objects.filter(order=order, product=product)) == 0:
                OrderItem.objects.create(order=order, product=product)


            else:
                existing_item = OrderItem.objects.get(order=order, product=product)
                existing_item.quantity = existing_item.quantity + 1
                existing_item.save()
            return redirect(product.get_absolute_url())

        else:
            context={'form':bound_form}
            return render(request,self.template_name,context=context)



@custom_permission_required('onlinestore.add_review')
class ProductAdd(View):
    '''Class to construct a view to add Product objects'''

    model=Product
    template_name='onlinestore/product_add.html'
    form_class=ProductForm

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class()})

    def post(self,request):
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            new_product=bound_form.save()
            return redirect(new_product.get_absolute_url())
        else:
            return render(request,self.template_name,{'form':bound_form})



@custom_permission_required('onlinestore.change_product')
class ProductUpdate(View):
    '''Class to construct a view to change a Product object'''

    model=Product
    template_name='onlinestore/product_change.html'
    form_class=ProductForm

    def get(self,request,pk):
        product=get_object_or_404(self.model,pk=pk)
        return render(request,self.template_name,{'form':self.form_class(instance=product),'product':product})

    def post(self,request,pk):
        product=get_object_or_404(self.model,pk=pk)
        bound_form=self.form_class(request.POST,instance=product)
        if bound_form.is_valid():
            updated_product=bound_form.save()
            return redirect(updated_product.get_absolute_url())
        else:
            return render(request,self.template_name,{'form':bound_form,'product':product})




@custom_permission_required('onlinestore.delete_product')
class ProductDelete(View):
    '''Class to create a view for deleting Product objects'''

    model=Product
    template_name='onlinestore/product_delete.html'

    def get(self,request,pk):
        product=get_object_or_404(self.model,pk=pk)
        return render(request,self.template_name,{'product':product})

    def post(self,request,pk):
        product=get_object_or_404(self.model,pk=pk)
        product.delete()
        return redirect('product_list')



@custom_permission_required('onlinestore.delete_review')
class ReviewDelete(View):
    '''Class to construct a vierw to delete Review objects'''

    model=Review
    template_name='onlinestore/review_delete.html'

    def get(self,request,pk):
        review=get_object_or_404(self.model,pk=pk)
        return render(request,self.template_name,{'review':review})

    def post(self,request,pk):
        review=get_object_or_404(self.model,pk=pk)
        product=review.product
        review.delete()
        return redirect(product.get_absolute_url())



def search_products(request):
    model1=Product
    model2=Category
    template_name='onlinestore/search_result.html'

    if request.method == 'POST':
        searched=request.POST.get('searched')
        print(searched)
        if searched:
            product_searched=model1.objects.filter(name__icontains=searched)
            category_searched=model2.objects.filter(name__icontains=searched)
            context_dict={
                'products':product_searched,
                'categories':category_searched
            }
            return render(request,template_name,context=context_dict)
        else:
            return redirect('post_list')







