
from django.contrib import admin
from django.urls import path, re_path ,include

#seo
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import (
    BlogSitemap,
    Sitemap,
)

urlpatterns_main = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.user.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.blog.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

sitemaps = {
    'site':Sitemap(
        [
            'home_app:home'
        ]
    ),
    'blogs':BlogSitemap,
}

urlpatterns_sitemap = [
    path(
        'sitemap.xml', 
        sitemap,{'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]




urlpatterns = urlpatterns_main + urlpatterns_sitemap