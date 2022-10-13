from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     # return render(request, 'articles/new.html')
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    
    # article = Article(title=title, content=content)
    # article.save()

    # # return redirect(request, 'articles/index.html')
    # return redirect('articles:detail', article.pk)
    
    # form = ArticleForm(request.POST)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # print(f'에러: {form.errors}')
    else:
        form=ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
    
@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@login_required
@require_POST
def delete(request, pk):
    # article = Article.objects.get(pk=pk)
    # if request.method == 'POST':
    #     article.delete()
    #     return redirect('articles:index')
    # return redirect('articles:detail', article.pk)
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
    # form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    # return redirect('articles:detail', article.pk)
    return render(request, 'articles/update.html', context)