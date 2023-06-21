from django.urls import path
from .views import SignUpView, SignInView, SignOutView
from . import views

urlpatterns = [
    path('up', views.signup,name='up'),
    path('up/up',SignUpView.as_view()),
    path('in', views.signin,name='in'),
    path('in/in',SignInView.as_view()),
    path('out',SignOutView.as_view()),
] 
