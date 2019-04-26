from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author  = models.ForeignKey("auth.user",         on_delete = models.CASCADE, verbose_name = "Yazar",    related_name = "articles")
    category = models.ForeignKey("article.category", on_delete = models.CASCADE,   verbose_name = "Kategori", null=True, related_name = "articleList")
    title   = models.CharField(max_length = 50,      verbose_name = "Başlık", unique=True)
    content = RichTextField(config_name="default",   null=True, verbose_name="İçerik")
    created_date = models.DateTimeField(verbose_name = "Oluşturulma Tarihi", auto_now_add = True)
    slug = models.SlugField(blank=True, null=True,  editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, null=True, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey("auth.user", on_delete = models.CASCADE)
    content = models.TextField(verbose_name = "Yorum")
    created_date = models.DateTimeField(verbose_name = "Gönderildiği Tarih", auto_now_add = True)
    def __str__(self):
        return self.author

class Category(models.Model):
    title   = models.CharField(max_length = 50, verbose_name = "Kategori", unique=True)
    def __str__(self):
        return self.title
