from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index),
    path('about/', about),
    path("article/<str:slug>", article),
    path("author/<str:author>", getArticleByAuthor),
    path("search/", searchArticleByTitle),
    path("category/<str:category>", getArticleByCategory)
]