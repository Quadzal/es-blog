from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Article,Category
from .forms import CommentForm
# Create your views here.

def getCategoryList():
    categoryList = Category.objects.all()
    return categoryList

def index(request):
    article_list = get_list_or_404(Article)
    paginator = Paginator(article_list, 10)

    page = request.GET.get('page') or 1
    articles = paginator.get_page(page)

    categoryList = getCategoryList()
    return render(request, "article/index.html", {"articles":articles, "categories":categoryList})


def about(request):
    categoryList = getCategoryList()
    return render(request, "article/about.html", {"categories":categoryList})

def article(request, slug):
    article = get_object_or_404(Article, slug = slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.author = request.user
        comment.save()
        return redirect("/")
    categoryList = getCategoryList()
    context = {
        'form':form,
        'article':article,
        'categories':categoryList
    }
    
    return render(request, "article/article.html", context)

def getArticleByAuthor(request, author):
    author = get_object_or_404(User, username = author)
    author_article_list = author.articles.all()
    categoryList = getCategoryList()
    return render(request, "article/index.html", {"articles":author_article_list, "categories":categoryList})


def getArticleByCategory(request, category):
    category = get_object_or_404(Category, title = category)
    category_article_list = category.articleList.all()
    categoryList = getCategoryList()
    return render(request, "article/index.html", {"articles":category_article_list, "categories":categoryList})


def searchArticleByTitle(request):
    title = request.GET["title"]
    print(title)
    articles = Article.objects.filter(title__contains = title)
    categoryList = getCategoryList()
    return render(request, "article/index.html", {"articles":articles, "categories":categoryList})