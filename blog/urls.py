from django.urls import path
from . import views

#URLs for views

urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.index, name='index'),
]