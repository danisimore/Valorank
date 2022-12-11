from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import SignUpView, SignInView


urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]