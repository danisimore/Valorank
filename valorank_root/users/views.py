from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from .forms import LoginForm, CreateUser


class SignInView(LoginView):

    template_name = 'authentication/signin.html'
    form_class = LoginForm

class SignUpView(View):

    template_name = 'authentication/signup.html'

    def get(self, request):
        context = {
            'form': CreateUser()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateUser(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

