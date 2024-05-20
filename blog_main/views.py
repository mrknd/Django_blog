from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

from blogs.models import Category, Blog
from .forms import RegistrationForm


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-updated_at')
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request=request, template_name='home.html', context=context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request=request, template_name='register.html', context=context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request=request, template_name='login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect('home')