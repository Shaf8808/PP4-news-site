from .models import Comment, Article, Review, Release
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'featured_image', 'slug', 'excerpt', 'content', 'status',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'slug', 'review_date', 'score', 'image', 
                  'excerpt', 'content', 'status',)


class ReleaseForm(forms.ModelForm):
    class Meta:
        model = Release
        fields = ('name', 'release_image', 'release_date', 'platform',)
