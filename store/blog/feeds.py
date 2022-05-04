from datetime import datetime
from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from django.utils.feedgenerator import Rss201rev2Feed,Atom1Feed
from .models import Post

class BasePostFeed():
    title='Latest Store.com blog posts'
    link=reverse_lazy('post_list')
    description=subtitle=(
        'Stay on the date on the latest Store.com blog posts'
    )

    def items(self):
        #Uses Post.Meta.ordering
        return Post.objects.all()[:10]

    def item_title(self,item):
        return item.formated_title()

    def item_description(self,item):
        return item.format_text()

    def item_link(self,item):
        return item.get_absolute_url()



class AtomPostFeed(Feed,BasePostFeed):
    feed_type = Atom1Feed

class RssPostFeed(Feed,BasePostFeed):
    feed_type = Rss201rev2Feed