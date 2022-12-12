from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='articles'),
    path('detail/<int:pk>', views.ArticleDetailView.as_view()),
]