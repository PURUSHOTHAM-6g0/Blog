from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('<slug:slug>',views.BlogView.as_view(),name='blog_view'),
    path('main/',views.main.as_view(),name='main'),
    path('about/',views.about.as_view(),name='about'),
    path('',views.PostList.as_view(),name='index_page'),
]
