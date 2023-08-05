from django.shortcuts import render
from django.http import HttpResponse
from .models import News
from datetime import date


# test = News.objects.create(text="Тест новостей", date=date.today())


def index(request):
    news_bd = News.objects.filter(is_published=True).order_by('time_create').reverse()
    return render(request, 'news/index.html', {'News': news_bd})
