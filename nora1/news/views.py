from django.shortcuts import render,  get_object_or_404
from .models import News_post


# Create your views here.

def news_list(request):
    news = News_post.objects.all()  # Получаем все новости из базы данных
    return render(request, 'news/news_list.html', {'news': news})  # Передаем данные в шаблон

def news_detail(request, pk):
    news = get_object_or_404(News_post, pk=pk)  # Получаем новость по её ID или возвращаем 404
    return render(request, 'news/news_detail.html', {'news': news})  # Передаем данные в шаблон