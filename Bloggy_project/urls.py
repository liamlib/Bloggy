"""Bloggy_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import BlogView, ContactView, BaseView, AboutUs, BlogPosts, news, BlogPost, NewsPost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogView.as_view(), name="main-page"),
    path('home/', BlogView.as_view(), name="main-page"),
    path('contact/', ContactView.as_view(), name="contact-page"),
    path('base/', BaseView.as_view(), name="base"),
    path('about-us/' , AboutUs.as_view(), name= "about"),
    path('blog-posts/' , BlogPosts.as_view(), name= "posts"),
    path('blog-post/<int:pk>/' , BlogPost.as_view(), name = "post"),
    path('news/', news.as_view(), name="news"),
    path('news-post/<int:pk>/', NewsPost.as_view(), name="news-post"),
    path('tinymce/', include('tinymce.urls')),
]
