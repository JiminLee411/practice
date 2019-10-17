from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-id')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()
    context = {
        'article_form' : article_form,
    }
    return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article) # instance 안넣어주면 새 게시글로 저장돼!!
        if article_form.is_valid():
            article = article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article) # instance 안넣어주면 수정하기 전 데이터 안나와!!

    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

@require_POST
def comment_c(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', pk)

def comment_d(request, pk, pk_c):
    article = Article.objects.get(pk=pk)
    comment = Comment.objects.get(pk=pk_c)
    comment.delete()

    return redirect('articles:detail', pk)
