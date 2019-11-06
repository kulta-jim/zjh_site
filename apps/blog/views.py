# from itertools import chain

from django.shortcuts import render
from django.views import View
from django.core.handlers.wsgi import WSGIRequest

from apps.comment.forms import MyCustomForm
from .models import Article, Category, BaseCategory, Tag
from tools import get_pages, to_markdown


# Create your views here.

class IndexView(View):
    def get(self, request):
        # context = {'blog_list': Blog.objects.all()}
        article_list = Article.objects.all().order_by('-pageviews')
        rows = []
        for i in range(0, len(article_list), 3):
            blog_list = []
            for j in range(i, i + 3):
                try:
                    blog_list.append(article_list[j])
                except IndexError:
                    break
            rows.append(blog_list)
            if len(rows) >= 2:
                break
        context = {'rows': rows}
        return render(request, 'base-index.html', context=context)


class BlogView(View):
    def get(self, request):
        article_list = Article.objects.all().order_by('-pageviews')
        _page = request.GET.get('page', 1)
        category_list = Category.objects.all()
        context = get_pages(article_list, int(_page))
        context['categories'] = category_list
        return render(request, 'blog/blog.html', context)


class BlogDetail(View):
    def get(self, request, blog_id):
        article = Article.objects.get(id=blog_id)
        article.text = to_markdown(article.text)
        form = MyCustomForm()
        context = {'article': article, 'form': form}
        return render(request, 'blog/blog-detail.html', context)


class BaseCategoryView(View):
    def get(self, request: WSGIRequest, base_category_id):
        categories = Category.objects.filter(parent_id=base_category_id)
        article_list = Article.objects.filter(category__in=categories)
        _page = request.GET.get('page', 1)
        context = get_pages(article_list, int(_page))
        context['categories'] = categories
        return render(request, 'blog/blog.html', context)


class CategoryView(View):
    def get(self, request: WSGIRequest, category_id):
        article_list = Article.objects.filter(category_id=category_id)
        _page = request.GET.get('page', 1)
        context = get_pages(article_list, int(_page))
        return render(request, 'blog/blog.html', context)


class TagView(View):
    def get(self, request, tag_id):
        article_list = Article.objects.filter(tags=tag_id)
        _page = request.GET.get('page', 1)
        context = get_pages(article_list, int(_page))
        return render(request, 'blog/blog.html', context)


class FilterView(View):
    def get(self, request):
        # print(type(BaseCategory.objects.all()))
        context = {
            'category_list': BaseCategory.objects.all(),
            'tags': Tag.objects.filter()
        }
        return render(request, 'blog/quan_zhan_filter.html', context=context)
