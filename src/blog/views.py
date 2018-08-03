from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Article
from .forms import ArticleForm

# Create your views here.

def blog_list_view(request):
    queryset = Article.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "blog/article_list.html", context)

def blog_detail_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
        "object": obj
    }
    return render(request, "blog/article_detail.html", context)
