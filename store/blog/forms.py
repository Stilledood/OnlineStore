from django import forms
from .models import Post,Commnent
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    '''Class to construct a form for adding,changing and deleting post objects'''

    class Meta:
        model=Post
        fields='__all__'

    def clean_title(self):
        forbidden=['add','delete','change']
        new_title=self.cleaned_data['title']
        if new_title in forbidden:
            raise ValidationError("Title can not be: 'add','change' or 'delete'")
        return new_title


class CommnetForm(forms.ModelForm):
    '''Class to construct a form for adding,changing and deleting comment objects'''

    class Meta:
        model=Commnent
        fields=['text']



