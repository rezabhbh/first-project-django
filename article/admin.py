from django.contrib import admin
from .models import Article, Category


admin.site.site_header="مدیریت سایت"

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
    list_display = ('title', 'slug', 'position', 'status', 'parent')
    list_filter = ('position', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug':('title',)}
    ordering = ['parent']

admin.site.register(Category, CategoryAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'thumbnail_tag', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug":('title',)}
    actions = [make_publish, make_draft]
    ordering = ['publish']


admin.site.register(Article, ArticleAdmin)
