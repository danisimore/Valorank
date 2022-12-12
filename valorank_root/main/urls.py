from django.urls import path

from .views import IndexListView, AboutUsListView

urlpatterns = [
    path('', IndexListView.as_view(), name='home'),
    path('about/', AboutUsListView.as_view(), name='about'),
]