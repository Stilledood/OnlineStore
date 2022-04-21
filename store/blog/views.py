from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View
from .models import Post,Commnent
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import PostForm,CommnetForm



class PostList(View):
    '''Class to construct a view to display all post objects using paginations'''

    model=Post
    template_name='blog/post_list.html'
    paginated_by=5
    page_kwargs='page'

    def get(self,request):
        post_list=self.model.objects.all()
        paginator=Paginator(post_list,self.paginated_by)
        page_number=request.GET.get(self.page_kwargs)

        try:
            page=paginator.page(page_number)
        except PageNotAnInteger:
            page=paginator.page(1)
        except EmptyPage:
            page=paginator.page(paginator.num_pages)

        if page.has_previous():
            previous_page_url=f"?{self.page_kwargs}={page.previous_page_number()}"
        else:
            previous_page_url=None

        if page.has_next():
            next_page_url=f"?{self.page_kwargs}={page.next_page_number()}"
        else:
            next_page_url=None

        context={
            'has_other_pages':page.has_other_pages(),
            'paginator':paginator,
            'previous_page_url':previous_page_url,
            'next_page_url':next_page_url,
            'post_list':page
        }

        return render(request,self.template_name,context=context)


class PostDetails(View):
    '''Class to construct a view to display all details for a post object'''

    model=Post
    template_name='blog/post_details.html'
    form_class=CommnetForm

    def get(self,request,pk):
        post=get_object_or_404(self.model,pk=pk)
        return render(request,self.template_name,{'post':post,'form':self.form_class()})

    def post(self,request,pk):
        post=get_object_or_404(self.model,pk=pk)
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            new_comm=bound_form.save(commit=False)
            new_comm.post=post
            new_comm.author=self.request.user
            new_comm.save()
            return redirect(post.get_absolute_url())
        else:
            return render(request,self.template_name,{'post':post,'form':bound_form})



