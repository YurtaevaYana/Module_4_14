from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisements14
from .forms import Advertisements14Form
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    advertisements = Advertisements14.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == "POST": # если нам что-то послали
        form = Advertisements14Form(request.POST, request.FILES) # получаем присланный текст и файлы
        if form.is_valid(): # если форма правильная
            advertisement = Advertisements14(**form.cleaned_data) # обращаемся к базе данных, записываем туда объявление
            advertisement.user = request.user # и информацию об отправителе - пользователе
            advertisement.save() # сохраняем
            url = reverse('main-page') # создаём ссылку на начальную страницу
            return HttpResponseRedirect(url) # и отправляем пользователя по ней
    else: # если нам ничего не посылали
        form = Advertisements14Form() # просто смотрим на форму
    context = {'form' : form}
    return render(request, 'advertisement-post.html', context)