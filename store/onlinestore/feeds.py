from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.utils.feedgenerator import Rss201rev2Feed,Atom1Feed
from .models import Product

class BaseFeedMixin:

    title='Store.com new products'
    description=subtitle=(
        'New products added on Store.com'
    )
    link=reverse_lazy('product_list')

    def items(self):
        return Product.objects.all()[:10]

    def item_title(self,product):
        return product.format_name()

    def item_description(self,product):
        return product.format_description()

    def item_price(self,product):
        return product.format_price()




class AtomFeed(Feed,BaseFeedMixin):
    feed_type = Atom1Feed

class RssFeed(Feed,BaseFeedMixin):
    feed_type = Rss201rev2Feed

