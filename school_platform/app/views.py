from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html')


def news_list(request):
    news = Newsletter.objects.all()
    paginator = Paginator(news, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,

    }
    return render(request, "blog/blog.html", context)


def news_detail(request, news_id):
    if Newsletter.objects.filter(id=news_id):
        news = Newsletter.objects.filter(id=news_id).first

        context = {
            'new': news
        }

    return render(request, 'blog/blog-details.html', context)
