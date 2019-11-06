from django.contrib import admin

# Register your models here.
from apps.comment import models


class CommentAdmin(admin.ModelAdmin):
    exclude = ['user_img', 'user_name', 'create_time']


admin.site.register(models.BlogComment, CommentAdmin)
