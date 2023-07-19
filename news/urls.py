from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('<slug:slug>/edit_comment/<int:id>', views.UpdateComment.as_view(), name='update_comment'),
    path('<slug:slug>/delete_comment/<int:id>', views.DeleteComment.as_view(), name='erase_comment'),
    path('like/<slug:slug>', views.ArticleLike.as_view(), name='article_like'),
]
