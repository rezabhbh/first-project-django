from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Category
from django.views.generic import ListView, DetailView




# def Home(request, page=1):
#     article_list = Article.objects.published()
#     paginator = Paginator(article_list, 3)
#     # page = request.GET.get('page')
#     article = paginator.get_page(page)
#     args = {
#         "article":article
#     }
#     return render(request, 'tem-project/home.html', args)

class ArticleList(ListView):
    queryset = Article.objects.published()
    template_name = 'tem-project/home.html'
    paginate_by = 2



# def Detail(request, slug):
#     context = get_object_or_404(Article, slug=slug )
#     args = {"articles":context}
#     return render(request, 'tem-project/detail.html', args)

class ArticleDetail(DetailView):
    template_name = 'tem-project/detail.html'
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)



# def Category_list(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     article_list = category.article.published()
#     paginator = Paginator(article_list, 2)
#     # page = request.GET.get('page')
#     article = paginator.get_page(page)
#     args = {
#         "category":category,
#         "article":article
#     }
#     return render(request, 'tem-project/category.html', args)

class Category_list(ListView):
    template_name = 'tem-project/category.html'
    paginate_by = 2

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.article.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['category'] = category
        return context