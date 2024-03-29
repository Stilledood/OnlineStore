from .models import Order,OrderItem,ShippingAdress
from django.views.generic import View
from django.shortcuts import render,get_object_or_404,redirect,reverse
from onlinestore.models import Product
from .forms import UpdateCartItem,ShippingForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class Cart(View):
    '''Class to construct a view to display cart items'''
    template_name='shoppingcart/cart_details.html'

    @method_decorator(login_required())
    def get(self,request):
        user=request.user
        order,created=Order.objects.get_or_create(user=user,complete=False)
        items=order.orderitem_set.all()
        total=order.get_total()
        number_of_products=sum([product.quantity for product in items])
        context={
            'product_list':items,
            'total':total,
            'total_number_of_products':number_of_products

        }

        return render(request,self.template_name,context=context)



class EditCart(View):
    template_name='shoppingcart/cart_edit.html'
    form_class=UpdateCartItem
    model=OrderItem

    def get(self,request,pk):
        orderitem=get_object_or_404(self.model,pk=pk)
        return render(request,self.template_name,{'item':orderitem,'form':self.form_class()})

    def post(self,request,pk):
        orderitem=get_object_or_404(self.model,pk=pk)
        bound_form=self.form_class(request.POST,instance=orderitem)
        if bound_form.is_valid():
            new_item=bound_form.save()
            return redirect('cart_details')
        else:
            return render(request,self.template_name,{'form':bound_form,'item':orderitem})


class DeleteItem(View):

    model=OrderItem
    template_name='shoppingcart/delete_item.html'

    def get(self,request,pk):
        item=get_object_or_404(self.model,pk=pk)
        return render(request,self.template_name,{'item':item})

    def post(self,request,pk):
        item=get_object_or_404(self.model,pk=pk)
        item.delete()
        return redirect('cart_details')



class CartDelete(View):
    '''Class to construct a view to delete your cart items'''

    model=Order
    template_name='shoppingcart/empty_cart.html'

    def get(self,request):
        user=request.user
        order=get_object_or_404(self.model,user=user,complete=False)
        return render(request,self.template_name,{'order':order})

    def post(self,request):
        user = request.user
        order = get_object_or_404(self.model, user=user, complete=False)
        order.delete()
        return redirect('cart_details')



class ShippingView(View):
    '''Class to create a view to display shipping form'''

    model=ShippingAdress
    template_name='shoppingcart/shipping.html'
    form_class=ShippingForm

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class()})

    def post(self,request):
        user=request.user
        order,created=Order.objects.get_or_create(user=user,complete=False)
        bound_form=self.form_class(request.POST)

        if bound_form.is_valid() :

            shipping=bound_form.save(commit=False)
            shipping.user=user
            shipping.order=order
            shipping.save()
            return redirect('post_list')
        else:
            return render(request,self.template_name,{'form':bound_form})


