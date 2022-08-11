from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import login, logout
from django.utils.crypto import get_random_string
from .models import User
from .forms import LoginForm, RegisterForm

# Create your views here.

class LoginPageView(View):
    def get(self, request: HttpRequest):
        login_form = LoginForm()
        return render(request, 'account_module/login.html', context={'login_form': login_form})

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data.get('username')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(username__iexact=user_name).first()

            if user is not None:
                is_password_correct = user.check_password(user_pass)
                if is_password_correct:
                    login(request, user)
                    return redirect(reverse('home-page'))
            else:
                login_form.add_error('username', 'There is no account with this information!')

        return render(request, 'account_module/login.html', context={'login_form': login_form})


class RegisterPageView(View):
    def get(self, request: HttpRequest):
        register_form = RegisterForm()
        return render(request, 'account_module/register.html', context={'register_form': register_form})

    def post(self, request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = register_form.cleaned_data.get('username')
            user_email = register_form.cleaned_data.get('email')
            user_pass = register_form.cleaned_data.get('password')

            user: bool = User.objects.filter(username__iexact=user_name).exists()
            if user:
                register_form.add_error('user_name', 'There is already a user with this information!')
            elif len(user_pass) < 8:
                register_form.add_error('password', 'Your password is too short!')
            else:
                new_user = User(
                    email=user_email,
                    email_activation_code=get_random_string(65),
                    is_active=False,
                    username=user_name)
                new_user.set_password(user_pass)
                new_user.save()
                return redirect(reverse('login-page'))
        return render(request, 'account_module/register.html', context={'register_form': register_form})


def logOut(request):
    logout(request)
    return redirect(reverse('login-page'))
    