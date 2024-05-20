from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from blogs.models import Category, Blog
from .forms import CategoryForm


@login_required(login_url='login')
def dashboard(request):
    categories_count = Category.objects.all().count()
    posts_count = Blog.objects.all().count()
    context = {
        'categories_count': categories_count,
        'posts_count': posts_count,
    }
    return render(request=request, template_name='dashboard/dashboard.html', context=context)


def categories(request):
    return render(request=request, template_name='dashboard/categories.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request=request, template_name='dashboard/add_category.html', context=context)


def edit_category(request, pk):
    # To show name of category in field Edit Category
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request=request, template_name='dashboard/edit_category.html', context=context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')