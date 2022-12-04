from django.urls import path

from .views import IndexView, AboutUsView, HomePageProductsView, HomePageArticles

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('api/v1/main/products', HomePageProductsView.as_view()),
    path('api/v1/main/articles', HomePageArticles.as_view()),
]