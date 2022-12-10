from django.urls import path, include
from .views import SignUpView, SignInView


urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
]