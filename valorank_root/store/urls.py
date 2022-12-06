from django.urls import path

from . import views

urlpatterns =[
    path('', views.StoreFormView.as_view(), name='store'),
    path('api/v1/products/all', views.ProductsAPIView.as_view()),
    path('api/v1/product/detail/<int:pk>', views.ProductDetailAPIView.as_view()),
    path('api/v1/base/ranks', views.BaseRanksAPIView.as_view()),
    path('api/v1/desired/ranks', views.DesiredRanksAPIView.as_view()),
]