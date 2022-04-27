from django.contrib import admin
from .models import Post,Commnent
from django.db.models import Count


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Class to create a custom admin post'''

    list_display=('title','date_added','author','tag_count')
    date_hierarchy = 'date_added'
    list_filter=('date_added',)
    search_fields = ('title','author',)

    fieldsets = (
        ('Principal',{
        'fields':('title','text','image')
        }),
    ('Related',{
    'fields':('tags','products','author')
    }),

    )
    filter_horizontal = ('tags','products',)

    def get_queryset(self, request):
        queryset=super().get_queryset(request)
        return queryset.annotate(tag_number=Count('tags'))

    def tag_count(self,post):
        return post.tags.count()
    tag_count.short_description='Number of tags'





