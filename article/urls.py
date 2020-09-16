from django.urls import path
from .views import Home ,Detail ,Category

app_name = 'article'
urlpatterns = [
    path('', Home, name='home'),
    path('detail/<slug:slug>', Detail, name='detail'),
    path('category/<slug:slug>', Category, name='category'),
]