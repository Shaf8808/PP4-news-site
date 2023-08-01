from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
# For update comments view
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic, View
from django.http import HttpResponseRedirect, Http404
from .models import Article, Release, Review, Comment
from .forms import CommentForm, ArticleForm, ReviewForm, ReleaseForm


class ArticleList(generic.ListView):
    context_object_name = 'article_list'
    template_name = 'index.html'
    queryset = Article.objects.filter(status=1).order_by('-created_on')
   
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleList, self).get_context_data(*args, **kwargs)
        context['release_list'] = Release.objects.order_by("-release_date")
        return context


class PostArticle(LoginRequiredMixin, generic.CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'add_article.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('home')


class EditArticle (LoginRequiredMixin, 
                   generic.UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'edit_article.html'

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('home')


class DeleteArticle(LoginRequiredMixin, generic.DeleteView):
    model = Article
    template_name = 'delete_article.html'
    
    def get_success_url(self):
        return reverse('home')


class ReviewList(generic.ListView):
    # View for displaying list of reviews on the review page
    model = Review
    queryset = Review.objects.filter(status=1).order_by("review_date")
    template_name = "reviews.html"
    paginate_by = 7


class PostReview(LoginRequiredMixin, generic.CreateView):
    form_class = ReviewForm
    template_name = 'add_review.html'

    def form_valid(self, form):
        form.instance.reviewer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('review_list')


class EditReview (LoginRequiredMixin, 
                  generic.UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'edit_review.html'

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('review_list')


class PostRelease(LoginRequiredMixin, generic.CreateView):
    form_class = ReleaseForm
    template_name = 'add_release.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class EditRelease (LoginRequiredMixin, 
                   generic.UpdateView):
    model = Release
    form_class = ReleaseForm
    template_name = 'edit_release.html'

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('home')


class DeleteRelease(LoginRequiredMixin, generic.DeleteView):
    model = Release
    template_name = 'delete_release.html'
    
    def get_success_url(self):
        return reverse('home')


class DeleteReview(LoginRequiredMixin, generic.DeleteView):
    model = Review
    template_name = 'delete_review.html'
    
    def get_success_url(self):
        return reverse('review_list')


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
            comment_form.instance.user = request.user
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
        

class UpdateComment(
        LoginRequiredMixin, UserPassesTestMixin, 
        generic.UpdateView
        ):

    """
    This view is used to allow logged in users to edit their own comments
    """
    model = Comment
    fields = ['body']
    template_name = 'edit_comment.html'

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('article_detail', kwargs={'slug': self.object.article.slug})

    def get_object(self, queryset=None):
        comment_id = self.kwargs['id']
        queryset = queryset or self.get_queryset()
        comment = get_object_or_404(queryset, id=comment_id, user=self.request.user)
        return comment

    def test_func(self):
        
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False


class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = 'delete_comment.html'

    def get_object(self, queryset=None):
        comment_id = self.kwargs['id']
        queryset = queryset or self.get_queryset()
        comment = get_object_or_404(queryset, id=comment_id, user=self.request.user)
        return comment

    def test_func(self):
        # Prevents another user from deleting someone else's
        # comment
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('article_detail', kwargs={'slug': self.object.article.slug})


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
    


class ReviewDetail(View):
    # View for displaying the content of the selected review
    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.review_comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),

            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.review_comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # Retrieves user data such as their email and username
            comment_form.instance.user = request.user
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            # First assigns an article to the comment before saving
            comment.review = review
            comment.save()
        else:
            # Returns an empty comment form instance if it is NOT valid
            comment_form = CommentForm()
        
        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),

            },
        )




class UpdateReviewComment(
        LoginRequiredMixin, UserPassesTestMixin, 
        generic.UpdateView
        ):

    """
    This view is used to allow logged in users to edit their own comments
    """
    model = Comment
    fields = ['body']
    template_name = 'edit_review_comment.html'

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('review_detail', kwargs={'slug': self.object.review.slug})

    def get_object(self, queryset=None):
        comment_id = self.kwargs['id']
        queryset = queryset or self.get_queryset()
        comment = get_object_or_404(queryset, id=comment_id, user=self.request.user)
        return comment

    def test_func(self):
        
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False


class DeleteReviewComment(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = 'delete_review_comment.html'

    def get_object(self, queryset=None):
        comment_id = self.kwargs['id']
        queryset = queryset or self.get_queryset()
        comment = get_object_or_404(queryset, id=comment_id, user=self.request.user)
        return comment

    def test_func(self):
        # Prevents another user from deleting someone else's
        # comment
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('review_detail', kwargs={'slug': self.object.review.slug})

        
class ReviewLike(View):

    def post(self, request, slug):
        # Retrieves specific review
        review = get_object_or_404(Review, slug=slug)
        # Checks to see if article has already been liked
        # before removing it
        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        # Adds like if it has not been liked
        else:
            review.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('review_detail', args=[slug]))
