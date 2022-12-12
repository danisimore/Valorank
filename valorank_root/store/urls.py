from django.urls import path

from . import views

urlpatterns =[
    path('', views.StoreFormView.as_view(), name='store'),
]