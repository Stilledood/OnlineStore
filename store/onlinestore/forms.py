from django import forms
from .models import Tag,Product,Category,Review
from django.core.exceptions import ValidationError


class CategoryForm(forms.ModelForm):
    '''Class to construct a form for Category object'''

    class Meta:
        model=Category
        fields='__all__'

    def clean_slug(self):
        forbidden=['add','delete','update','create','delete']
        new_slug=self.cleaned_data['slug'].lower()
        if new_slug in forbidden:
            raise ValidationError("Slug can not be :'add','delete','update','create' or 'delete' !")
        return new_slug



class TagForm(forms.ModelForm):
    '''Class to construct a form for Tag Objects'''

    class Meta:
        model=Tag
        fields='__all__'

    def clean_slug(self):
        forbidden = ['add', 'delete', 'update', 'create', 'delete']
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug in forbidden:
            raise ValidationError("Slug can not be :'add','delete','update','create' or 'delete' !")
        return new_slug


class ProductForm(forms.ModelForm):
    '''Class to construct a form for Product objects '''

    class Meta:
        model=Product
        fields='__all__'

    def clean_name(self):
        forbidden=['add','delete','update']
        new_name=self.cleaned_data['name']
        if new_name in forbidden:
            raise ValidationError("Name can not be: 'add','delete','update'")
        return new_name



class ReviewForm(forms.ModelForm):
    '''Class to construct a form for Review objects'''

    class Meta:
        model=Review
        fields=['body']
