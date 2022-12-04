from django.urls import path
from .views import IndexView, HomePageProductsView, HomePageArticles

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

urlpatterns = [
    path('', IndexView.as_view()),
    path('api/v1/main/products', HomePageProductsView.as_view()),
    path('api/v1/main/articles', HomePageArticles.as_view()),
]