from django.contrib import admin
from .models import Advertisements14

class Advertisements14Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'connection', 'created_date', 'updated_date', 'image'] # отвечает за то, какие толбцы таблицы будут показаны в админке
    list_filter = ['auction', 'created_time'] # задает поля для фильтрации (можем выбрать их из столбцов таблицы) - они будут справа на сайте
    actions = ['make_auction_as_false', 'make_auction_as_true'] # задает список функций, которые будут реализованы в выпадающем списке для выделенных строк таблицы
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'connection', 'image'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    ) # задает разбиение поля заполнения объявления на смысловые блоки

    @admin.action(description='Убрать возможность торга') # а это и следующее - функции для actions, прописываются ниже остального кода
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisements14, Advertisements14Admin) # здесь мы говорим "пусть содержимое будет от таблицы Advertisements14, а доп функционал - от класса Advertisements14Admin
