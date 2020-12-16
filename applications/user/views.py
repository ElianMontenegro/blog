from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    CreateView
)

from django.views.generic.edit import (
    FormView
)

from .forms import (
    UserRegisterForm,
    LoginForm
)
from .models import User
# 


class UserRegisterView(FormView):
    template_name = 'user/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            full_name=form.cleaned_data['full_name'],       
        )
        # enviar el codigo al email del user
        return super(UserRegisterView, self).form_valid(form)

class LoginUser(FormView):
    template_name = 'user/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('panel_app:index')

    def form_valid(self, form):
        user = authenticate(
            #con el autenticate se verifica que exista este usuario
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)

class LogOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'panel_app:index'                
            )
        )