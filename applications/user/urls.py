from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'register/', 
        views.UserRegisterView.as_view(),
        name='register',
    ),
    path(
        'login/', 
        views.LoginUser.as_view(),
        name='login',
    ),
    path(
        'logout/', 
        views.LogOutView.as_view(),
        name='logout',
    ),
]