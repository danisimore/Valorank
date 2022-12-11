from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View

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

