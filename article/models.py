from django.db import models
from django.utils import timezone
from django.utils.html import format_html


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100,unique=True, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=False, verbose_name="آیا نمایش داده شود ؟")
    position = models.IntegerField(verbose_name="پوزیشن")


    class Meta():
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title



class Article(models.Model):
    CHOICES_STATUS =[
        ('p', 'منتشر شده'),
        ('d', 'پیش نویس'),
    ]

    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=150, unique=True, verbose_name="آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name="article")
    description = models.TextField(verbose_name="محتوای مقاله")
    thumbnail = models.ImageField(upload_to="images", blank=True, verbose_name="عکس مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=CHOICES_STATUS, verbose_name="وضعیت")


    class Meta():
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def thumbnail_tag(self):
        return format_html('<img src={} width=100>',format(self.thumbnail.url))
    thumbnail_tag.short_description = "عکس"