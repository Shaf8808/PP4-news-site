from django.contrib import admin
from .models import Article, Comment, Release, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')
    actions = ['publish_articles']

    # Give option to quickly publish draft articles from panel
    def publish_articles(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    search_fields = ('name', 'email', 'body')
    list_display = ('name', 'body', 'article', 'review', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):

    search_fields = ('name', 'platform', 'release_date')
    list_display = ('name', 'release_date', 'platform')
    list_filter = ('platform', 'release_date')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'score', 'content', 'reviewer')
    list_display = ('title', 'score', 'reviewer')
    list_filter = ('title', 'score', 'reviewer')
    summernote_fields = ('content')
