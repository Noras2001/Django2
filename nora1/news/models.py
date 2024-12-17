from django.db import models
from django.contrib.auth.models import User  # Импортируем модель пользователя

class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)  # Добавлено auto_now_add
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор новости')  # Поле пользователя

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
