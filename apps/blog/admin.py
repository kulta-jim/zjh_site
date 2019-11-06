from django.contrib import admin
from mdeditor.widgets import MDEditorWidget
from django.db import models

from . import models as demo_models


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'summary', 'category', 'tags', 'img', 'is_original', 'text')
    exclude = ('author', 'pageviews',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug', 'article_number')


class BaseCategoryAdmin(admin.ModelAdmin):
    exclude = ('slug', 'article_number')


class TagAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(demo_models.BaseCategory, BaseCategoryAdmin)
admin.site.register(demo_models.Tag, TagAdmin)
admin.site.register(demo_models.Article, ArticleAdmin)
admin.site.register(demo_models.Category, CategoryAdmin)
