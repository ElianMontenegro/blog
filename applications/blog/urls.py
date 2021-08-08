from django.urls import path

from . import views

app_name = "blog_app"

urlpatterns = [
    path(
        'detail/<slug>/', 
        views.BlogDetailView.as_view(),
        name='detail-blog',
    ),
    path(
        'list-blogs/', 
        views.BlogListView.as_view(),
        name='list-blog',
    ),
]