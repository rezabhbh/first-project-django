from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Category




def Home(request, page=1):
    article_list = Article.objects.published()
    paginator = Paginator(article_list, 3)
    # page = request.GET.get('page')
    article = paginator.get_page(page)
    args = {
        "article":article
    }
    return render(request, 'tem-project/home.html', args)


def Detail(request, slug):
    context = get_object_or_404(Article, slug=slug )
    args = {"articles":context}
    return render(request, 'tem-project/detail.html', args)