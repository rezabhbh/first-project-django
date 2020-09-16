from django.shortcuts import render, get_object_or_404
from .models import Article, Category



def Home(request):
    context = Article.objects.filter(status='p')
    args = {"article":context}
    return render(request, 'tem-project/home.html', args)


def Detail(request, slug):
    context = get_object_or_404(Article, slug=slug )
    args = {"articles":context}
    return render(request, 'tem-project/detail.html', args)

def Category(request, slug):
    context = get_object_or_404(Article, slug=slug)
    args = {"category":context}
    return render(request, 'tem-project/detail.html', args)