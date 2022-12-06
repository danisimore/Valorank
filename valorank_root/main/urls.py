from django.urls import path

from .views import IndexListView, AboutUsListView, HomePageProductsAPIView, HomePageArticlesAPIView

urlpatterns = [
    path('', IndexListView.as_view(), name='home'),
    path('about/', AboutUsListView.as_view(), name='about'),
    path('api/v1/main/products', HomePageProductsAPIView.as_view()),
    path('api/v1/main/articles', HomePageArticlesAPIView.as_view()),
]