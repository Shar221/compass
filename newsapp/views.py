from django.shortcuts import render, redirect   
from .models import NewsArticle, Category, Comment
from .forms import NewsArticleForm, UpdateNewsArticleForm

def index(request):
    articles = NewsArticle.objects.all().order_by('-published_at')[:5]
    context = {'articles': articles}    
    
    return render(request, 'newsapp/index.html', context)

def article_detail(request, article_id):
    article = NewsArticle.objects.get(id=article_id)
    comments = article.comments.all().order_by('-created_at')
    context = {'article': article, 'comments': comments}
    
    return render(request, 'newsapp/article_detail.html', context)

def create_news_article(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            news_article = form.save(commit=False)
            news_article.writer = request.user
            news_article.save()
            return redirect('index')
    else:
        form = NewsArticleForm()
    
    return render(request, 'newsapp/create_article.html', {'form': form})

def update_news_article(request, article_id):
    article = NewsArticle.objects.get(id=article_id)
    if request.method == 'POST':
        form = UpdateNewsArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = UpdateNewsArticleForm(instance=article)
    
    return render(request, 'newsapp/update_article.html', {'form': form, 'article': article})