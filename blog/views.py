from multiprocessing import context

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, New
# Create your views here.

class BlogView(ListView):
    template_name = "index.html"
    model = Post


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()  # list
        return context



class ContactView(TemplateView):
    template_name = "contact.html"

class BaseView(TemplateView):
    template_name = "base.html"

class AboutUs(TemplateView):
    template_name = "about.html"

class BlogPosts(ListView):
    template_name = "posts.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()  # list
        return context

class BlogPost(DetailView):
    template_name = "post.html"
    model = Post

    def get_object(self, queryset=None):
        return super().get_object()

    def get_context_data(self, **kwargs):
        obj = self.get_object()
        context = super().get_context_data(**kwargs)
        context['title'] = obj.title
        context['subheading'] = obj.subheading
        context['author'] = obj.author
        context['content'] = obj.content
        context['published_date'] = obj.published_date

        print(obj.subheading)
        return context

class news(ListView):
    template_name = "news.html"
    model = New

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = New.objects.all()  # list
        return context

class NewsPost(DetailView):
    template_name = "news_item.html"
    model = New

    def get_object(self, queryset=None):
        return super().get_object()

    def get_context_data(self, **kwargs):
        obj = self.get_object()
        context = super().get_context_data(**kwargs)
        context['title'] = obj.title
        context['subheading'] = obj.subheading
        context['author'] = obj.author
        context['content'] = obj.content
        context['published_date'] = obj.published_date

        print(obj.subheading)
        return context


