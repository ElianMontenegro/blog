from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.

from django.views.generic import (
    TemplateView,
    CreateView,
)
from applications.blog.models import Blog
from applications.home.models import Suscriber
from .forms import SuscriberForm

class Home(TemplateView):
    template_name = "home/index.html"
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.blog_portada()
        context['in_home'] = Blog.objects.blog_in_home()
        context['medium'] = Blog.objects.blog_medium()
        
        return context
   
class SuscribersCreateView(CreateView):
    form_class = SuscriberForm
    success_url = reverse_lazy('home_app:home')
    template_name = "home/index.html"
   
    