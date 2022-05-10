from datetime import date
from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemaps(Sitemap):
    '''Class to construct the sitempa for post model'''

    changefreq='never'
    priority=0.5

    def items(self):
        return Post.objects.published()

    def lastmod(self,post):
        return post.date_added

