from django import forms


class ProductAddToCartForm(forms.Form):
    '''form class to add products to the shoping cart'''
    quantity=forms.IntegerField(widget=forms.TextInput(attrs={'value':'1','class':'quantity'}))

    def __init__(self,request=None,*args,**kwargs):
        self.request=request
        super(ProductAddToCartForm,self).__init__(*args,**kwargs)

    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError('Cookies must be enabled')
            return  self.cleaned_data
