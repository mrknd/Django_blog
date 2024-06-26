from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import Blog, Category, Comment


def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    # try:
    #     category = Category.objects.get(id=category_id)
    # except:
    #     return redirect('home')
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request=request, template_name='posts_by_category.html', context=context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')

    # Comments Form
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST.get('comment')
        comment.save()
        # Take back to page where we were
        return HttpResponseRedirect(request.path_info)


    # Comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request=request, template_name='blogs.html', context=context)


def search(request):
    keyword = request.GET.get('keyword')
    blog_search = Blog.objects.filter(Q(title__icontains=keyword) |
                                      Q(blog_body__icontains=keyword) |
                                      Q(short_description__icontains=keyword),
                                      status='Published')
    context = {
        'blog_search': blog_search,
        'keyword': keyword,
    }
    return render(request=request, template_name='search.html', context=context)