from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from onlinestore.models import Tag,Product
from datetime import date


class PostQueryset(models.QuerySet):
    '''Class to define a custom queryset'''

    def published(self):
        return self.filter(date_added__lte=date.today())



class Post(models.Model):
    '''Class to construct a model for Post objects'''

    title=models.CharField(max_length=256)
    text=models.TextField()
    date_added=models.DateField(auto_now_add=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blog_images',default=None)
    tags=models.ManyToManyField(Tag)
    products=models.ManyToManyField(Product)
    objects=PostQueryset.as_manager()

    class Meta:
        ordering=['-date_added','title']
        get_latest_by='title'
        permissions = (
            ('view_future_post', 'Can view unpublished posts'),
        )
    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('post_details',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('post_update',kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('post_delete',kwargs={'pk':self.pk})



class Commnent(models.Model):
    '''Class to create a model for commnet object'''

    text=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_added=models.DateField(auto_now_add=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    class Meta:
        ordering=['-date_added']
        get_latest_by='date_added'


    def __str__(self):
        return self.text[:50]

    def get_delete_url(self):
        return reverse('commnet_delete',kwargs={'pk':self.pk})



