from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='articles'),
    path('detail/<int:pk>', views.ArticleDetailView.as_view()),
    path('api/v1/articles/all', views.ArticlesAPIView.as_view()),
    path('api/v1/article/categories', views.ArticleCategoriesAPIView.as_view()),
    path('api/v1/article/detail/<int:pk>', views.ArticleDetailAPIView.as_view())
]