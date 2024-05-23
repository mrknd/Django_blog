from django.contrib import admin

from .models import Category, Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'is_featured', 'status')
    search_fields = ('title', 'short_description', 'blog_body', 'category__category_name', 'status')
    list_editable = ('is_featured',)


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)




