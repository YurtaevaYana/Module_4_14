from django.urls import path
from .views import lesson_4 # подгрузили функцию lesson_4 из файла views

urlpatterns = [
    path('', lesson_4) # дописали текстовый ответ к корневому пути (ссылке, которая появляется в терминале)
]