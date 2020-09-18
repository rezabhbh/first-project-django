from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from article.models import Article

@login_required
def home(request):
    return render(request, 'registration/home.html')


class ArticleList(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'
    queryset = Article.objects.all()