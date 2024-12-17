#from django.contrib import admin
#from .models import News_post

# Register your models here.

#admin.site.register(News_post)

from django.contrib import admin
from .models import News_post

@admin.register(News_post)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'pub_date', 'author')  # Поля, которые будут видны в списке
    search_fields = ('title', 'text')  # Добавляет возможность поиска
    list_filter = ('pub_date', 'author')  # Фильтры по дате и автору

