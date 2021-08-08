from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import Blog,Category


class BlogDetailView(DetailView):
    template_name = "blog/detail_blog.html"
    model = Blog


class BlogListView(ListView):
    template_name = "blog/list_blog.html"
    context_object_name = "blogs"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        category = self.request.GET.get("category", '') 
        result = Blog.objects.search_blog(kword, category)
        return result
    
    
   
