from django.urls import path
from .views import index, top_sellers # подгрузили функции index, top_sellers из файла views

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers')
]