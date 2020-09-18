from django.urls import path
from .views import ArticleList , ArticleDetail, Category_list

app_name = 'article'
urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    path('page/<int:page>', ArticleList.as_view(), name='home'),
    path('detail/<slug:slug>', ArticleDetail.as_view(), name='detail'),
    path('category/<slug:slug>', Category_list.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>', Category_list.as_view(), name='category'),
]