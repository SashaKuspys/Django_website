from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    context = {
        'title': 'Головна сторінка',
        'content': 'Trans Build Invest'
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Про нас',
        'content': 'Trans Build Invest',
        'text_on_page': 'Текст на сторінці про нас'
    }
    return render(request, 'main/about.html', context)