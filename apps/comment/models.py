from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.

class LeaveWord(models.Model):
    c_name = models.CharField(max_length=20, verbose_name='留言者')
    c_email = models.EmailField(verbose_name='留言邮箱')
    c_message = models.CharField(verbose_name='留言', max_length=500)

    def __str__(self):
        return f"{self.c_name}'s message"

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    class Meta:
        abstract = True
        verbose_name = '评论Model'
        verbose_name_plural = verbose_name

    author = models.ForeignKey('my_accounts.SiteUser', on_delete=models.CASCADE, related_name='comment_user')
    context = MDTextField(verbose_name='评论内容')
    create_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    user_name = models.CharField(max_length=50, verbose_name='评论者')
    user_img = models.CharField(max_length=200, verbose_name='评论者头像位置')

    def save(self, *args, **kwargs):
        self.user_name = self.author.username
        self.user_img = self.author.user_img.url
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.author.username}'s comments"


class BlogComment(Comment):
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE, related_name='article_comment')
