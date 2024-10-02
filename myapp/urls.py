from django.urls import path # type: ignore 
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # For the input form
    path('register/', views.register, name='register'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout, name='logout'),
    path('post/<str:pk>/', views.post, name='post')

]


