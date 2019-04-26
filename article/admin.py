from django.contrib import admin
from .models import Article,Category
# Register your models here.



class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","created_date","author"]
    list_filter  = ["title","created_date"]


admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)