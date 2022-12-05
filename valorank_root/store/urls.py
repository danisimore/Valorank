from django.urls import path

from store.views import StoreFormView

urlpatterns =[
    path('', StoreFormView.as_view(), name='store'),
]