'''from django.urls import path 
from . import views

urlpatterns = [
    path("login", views.login_request,name="login"),
    path("register", views.register_request ,name="register"),
    path("logout", views.logout_request,name="logout")
]'''
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
