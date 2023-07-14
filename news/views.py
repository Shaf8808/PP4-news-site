from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Article, Release, Review


class ArticleList(generic.ListView):
    context_object_name = 'article_list'
    template_name = 'index.html'
    queryset = Article.objects.filter(status=1).order_by('-created_on')
   
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleList, self).get_context_data(*args, **kwargs)
        context['release_list'] = Release.objects.order_by("-release_date")
        return context


class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by('created_on')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "article_detail.html",
            {
                "article": article,
                "comments": comments,
                "liked": liked,

            },
        )
