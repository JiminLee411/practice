from django.contrib import admin
from .models import Article, Comment
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'updated_at', 'created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)