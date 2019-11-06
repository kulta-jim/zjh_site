from django.db import models
# from django.template.defaultfilters import slugify
from django.db.models import Q
from mdeditor.fields import MDTextField
from uuslug import slugify
from itertools import chain


# Create your models here.




class Article(models.Model):
    blog_type = ((0, '转载'),
                 (1, '原创'))

    class Meta:
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name
        ordering = ['-update_time']

    title = models.CharField(max_length=50, verbose_name='标题')
    author = models.ForeignKey('my_accounts.SiteUser', verbose_name='作者', on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='博客图片', upload_to='blog_img', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_original = models.BooleanField(choices=blog_type, verbose_name='是否原创')
    summary = models.CharField(max_length=200, verbose_name='摘要')
    text = MDTextField(verbose_name='正文')
    pageviews = models.IntegerField(default=0, verbose_name='浏览量')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='博客类别')
    tags = models.ManyToManyField('Tag', related_name='blog_tags', verbose_name='标签')

    def __str__(self):
        return self.title

    def pageviews_add(self):
        self.pageviews += 1
        self.save(update_fields=['pageviews'])


class AbstractCategory(models.Model):
    class Meta:
        abstract = True
        verbose_name = '抽象类'
        verbose_name_plural = verbose_name

    slug = models.SlugField()
    name = models.CharField(max_length=20, verbose_name='类别名')

    def __str__(self):
        return self.name


class BaseCategory(AbstractCategory):
    class Meta:
        verbose_name = '基础类别'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def get_article_number(self):
        article_number = 0
        categories = Category.objects.filter(parent=self)
        for category in categories:
            article_number += Article.objects.filter(category=category).count()
        return article_number

    def get_child_category(self):
        return Category.objects.filter(parent=self)


class Category(AbstractCategory):
    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    parent = models.ForeignKey('BaseCategory', on_delete=models.CASCADE, verbose_name='基础类别',
                               related_name='parent_category')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # self.article_number = Article.objects.filter(category=self).count()
        super().save(*args, **kwargs)

    def get_article_number(self):
        article_number = Article.objects.filter(category=self).count()
        return article_number


class Tag(models.Model):
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=20, verbose_name='标签名')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_article_number(self):
        article_number = Article.objects.filter(tags=self).count()
        return article_number

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
