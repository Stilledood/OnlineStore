from django.db import models
from django.shortcuts import redirect,render,reverse
from django.conf import settings


class Category(models.Model):
    '''Class to create a model for Category objects'''

    name=models.CharField(max_length=64)
    slug=models.SlugField(max_length=32,unique=True)
    image=models.ImageField(upload_to='category_images',null=True)

    class Meta:
        ordering=['name']
        get_latest_by='name'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_details',kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('category_change',kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('category_delete',kwargs={'slug':self.slug})


class Tag(models.Model):
    '''Class to create a model for Tag objects'''

    name=models.CharField(max_length=64)
    slug=models.CharField(max_length=32,unique=True)

    class Meta:
        ordering=['name']
        get_latest_by='name'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_details',kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('tag_change',kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('tag_delete',kwargs={'slug':self.slug})


class Product(models.Model):
    '''Class to create a model for Product objects'''

    name=models.CharField(max_length=256)
    description=models.TextField()
    date_added=models.DateField(auto_now_add=True)
    dimensions=models.CharField(max_length=128)
    weight=models.FloatField()
    image=models.ImageField(upload_to='product_images')
    price=models.FloatField()
    featured=models.BooleanField(default=False)
    reduced_price=models.BooleanField(default=False)
    new_price=models.FloatField(default=None)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag)

    class Meta:
        ordering=['-date_added','name']
        get_latest_by='date_added'

    def __str__(self):
        return self.name[:20]

    def get_absolute_url(self):
        return reverse('product_details',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('product_change',kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('product_delete',kwargs={'pk':self.pk})

    def format_name(self):
        return self.name.title()

    def format_description(self):
        if len(str(self.description)) > 20:
            short=str(self.description)[:20]+'.......'
            return short
        else:
            return str(self.description)

    def format_price(self):
        return (self.price +'USD')


class Review(models.Model):
    '''Class to construct a model for reviews objects'''

    body=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-date_added']
        get_latest_by='date_added'

    def __str__(self):
        return self.body[:20]

    def get_delete_url(self):
        return reverse('review_delete',kwargs={'pk':self.pk})












