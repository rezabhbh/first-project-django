from django.contrib import admin
from .models import Article, Category


def make_publish(modeladmin, request, queryset):
    rows_updated = queryset.update(status = 'p')
    if rows_updated == 1:
        message="شد"
    else:
        message="شدند"
    modeladmin.message_user(request, f"{rows_updated} مقاله منتشر {message}")
make_publish.short_description = "انتشار مقاله"

def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status = 'd')
    if rows_updated == 1:
        message = "شد"
    else:
        message = "شدند"
    modeladmin.message_user(request, f"{rows_updated} مقاله پیش نویس {message}")
make_draft.short_description = "پیش نویس مقاله"



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'position', 'status')
    list_filter = ('position', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug':('title',)}
    ordering = ['position']

admin.site.register(Category, CategoryAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'thumbnail_tag', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug":('title',)}
    actions = [make_publish, make_draft]
    ordering = ['publish']


admin.site.register(Article, ArticleAdmin)
