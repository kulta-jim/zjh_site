from django.contrib.auth.models import User, AbstractUser
from django.db import models
# from django.template.defaultfilters import slugify
from uuslug import slugify


# Create your models here.

class SiteUser(AbstractUser):
    area = (('北京市', 0),
            ('天津市', 1),
            ('上海市', 2),
            ('重庆市', 3),
            ('河北省', 4),
            ('山西省', 5),
            ('辽宁省', 6),
            ('吉林省', 7),
            ('黑龙江省', 8),
            ('江苏省', 9),
            ('浙江省', 10),
            ('安徽省', 11),
            ('福建省', 12),
            ('江西省', 13),
            ('山东省', 14),
            ('河南省', 15),
            ('湖北省', 16),
            ('湖南省', 17),
            ('广东省', 18),
            ('海南省', 19),
            ('四川省', 20),
            ('贵州省', 21),
            ('云南省', 22),
            ('陕西省', 23),
            ('甘肃省', 24),
            ('青海省', 25),
            ('西藏自治区', 26),
            ('广西壮族自治区', 27),
            ('内蒙古自治区', 28),
            ('宁夏回族自治区', 1),
            ('新疆维吾尔自治区', 29),
            ('香港特别行政区', 30),
            ('澳门特别行政区', 31),
            ('台湾省', 32))
    slug = models.SlugField(unique=True, editable=False)
    telephone = models.BigIntegerField(verbose_name='电话', blank=True, null=True)
    change_date = models.DateTimeField('更改时间', auto_now=True)
    address = models.CharField(verbose_name='地区', choices=area, max_length=10)
    industry = models.CharField(verbose_name='行业', max_length=20)
    position = models.CharField(verbose_name='职业', max_length=20)
    Introduction = models.CharField(verbose_name='简介', max_length=50)
    user_img = models.ImageField(verbose_name='头像', upload_to=f'user_img', blank=True, null=True,
                                 default='user_img/default.png', )

    class Meta:
        verbose_name = '用户资料'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
