from django.views.generic import DetailView, TemplateView, ListView, CreateView

from .models import Article, Category


class ListArticle(ListView):
    template_name = 'article/list.html'
    model = Article

    def get_queryset(self):
        return super().get_queryset().filter(categories__id__in=[self.kwargs['cat_id']])
