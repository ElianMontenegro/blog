from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy
from datetime import datetime
from applications.blog.models import Blog


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Blog.objects.filter(public=True)
    
    def lastmod(self, obj):
        return obj.created

class Sitemap(Sitemap):
    protocol = 'https'

    def __init__(self, names):
        self.names = names
    
    def changefreq(self, obj):
        return 'weekly'
    
    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return reverse_lazy(obj)


