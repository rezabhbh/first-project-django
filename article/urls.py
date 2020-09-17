from django.urls import path
from .views import Home , Detail, Category_list

app_name = 'article'
urlpatterns = [
    path('', Home, name='home'),
    path('page/<int:page>', Home, name='home'),
    path('detail/<slug:slug>', Detail, name='detail'),
    path('category/<slug:slug>', Category_list, name='category'),
    path('category/<slug:slug>/page/<int:page>', Category_list, name='category'),
]