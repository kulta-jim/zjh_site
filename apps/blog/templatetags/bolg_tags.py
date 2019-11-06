from django import template
from ..models import Category, Article

register = template.Library()


@register.simple_tag
def get_child_category(category_id=0):
    if category_id == 0:
        return Category.objects.all()
    else:
        return Category.objects.filter(parent_id=category_id)


@register.simple_tag
def get_category_article_count(category_id):
    all_child = Category.objects.filter()
    return Article.objects.filter(category_id=category_id).count()


# a = {
#     '1-1': {'2-1': {'3-1': ''}, '2-2': {'3-1': ''}},
#     '1-2': {'2-1': {'3-1': ''}, '2-2': {'3-1': ''}},
#     '1-3': {'2-1': {'3-1': ''}, '2-2': {'3-1': ''}}
# }
