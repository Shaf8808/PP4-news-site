from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('addarticle/', views.PostArticle.as_view(), name='add_article'),
    path('addreview/', views.PostReview.as_view(), name='add_review'),
    path('addrelease/', views.PostRelease.as_view(), name='add_release'),
    path('<slug:slug>/editrelease/', views.EditRelease.as_view(), name='edit_release'),  # noqa
    path('<slug:slug>/deleterelease/', views.DeleteRelease.as_view(), name='delete_release'),  # noqa
    path('<slug:slug>/deletereview/', views.DeleteReview.as_view(), name='delete_review'),  # noqa
    path('<slug:slug>/editreview/', views.EditReview.as_view(), name='edit_review'),  # noqa
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('<slug:slug>/edit_article/', views.EditArticle.as_view(), name='update_article'),  # noqa
    path('<slug:slug>/delete_article/', views.DeleteArticle.as_view(), name='delete_article'),  # noqa
    path('<slug:slug>/edit_review_comment/<int:id>', views.UpdateReviewComment.as_view(), name='update_review_comment'),  # noqa
    path('<slug:slug>/delete_review_comment/<int:id>', views.DeleteReviewComment.as_view(), name='erase_review_comment'),  # noqa
    path('reviews/<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),  # noqa
    path('<slug:slug>/edit_comment/<int:id>', views.UpdateComment.as_view(), name='update_comment'),  # noqa
    path('<slug:slug>/delete_comment/<int:id>', views.DeleteComment.as_view(), name='erase_comment'),  # noqa
    path('like/<slug:slug>', views.ArticleLike.as_view(), name='article_like'),
    path('reviews/like/<slug:slug>', views.ReviewLike.as_view(), name='review_like'),  # noqa
]
