from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Article, Release, Review
from .forms import CommentForm


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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),

            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by('created_on')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # Retrieves user data such as their email and username
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            # First assigns an article to the comment before saving
            comment.article = article
            comment.save()
        else:
            # Returns an empty comment form instance if it is NOT valid
            comment_form = CommentForm()
        
        return render(
            request,
            "article_detail.html",
            {
                "article": article,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),

            },
        )


class ArticleLike(View):

    def post(self, request, slug):
        # Retriieves specific article
        article = get_object_or_404(Article, slug=slug)
        # Checks to see if article has already been liked
        # before removing it
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        # Adds like if it has not been liked
        else:
            article.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('article_detail', args=[slug]))