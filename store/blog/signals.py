from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from onlinestore.models import Tag
from .models import Post


@receiver(m2m_changed,sender=Post.products.through)
def assign_extra_tags(sender,**kwargs):
    '''Function to create a signal to automatically assign all product tags to blog post '''

    action=kwargs.get('action')
    if action =='post_add':
        reverse=kwargs.get('reverse')
        if not  reverse:
            post=kwargs.get('instance')
            product_pk_list=kwargs.get('pk_set')
            tag_pk_list=Tag.objects.filter(product__in=product_pk_list).values_list('pk',flat=True).distinct().iterator()
            post.tags.add(*tag_pk_list)
        else:
            product=kwargs.get('instance')
            tag_pk_set=tuple(product.tag.value_list('pk',flat=True).iterator())
            PostModel=kwargs.get('model')
            post_pk_set=kwargs.get('pk_set')
            posts_dict=PostModel.objects.in_bulk(post_pk_set)
            for post in posts_dict.values():
                post.tags.add(*tag_pk_set)


