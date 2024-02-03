from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Мёд',
        'menu': ['Купить мед', 'Контакты', 'Фото', 'Видео', 'Документы'],
    }

    return render(request, template_name='main/index.html', context=context)

def about(request):
    return HttpResponse('About page')