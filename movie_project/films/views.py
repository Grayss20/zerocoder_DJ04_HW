from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm


# Главная страница с отображением всех фильмов
def index(request):
    films = Film.objects.all()
    return render(request, 'films/index.html', {'films': films})


# Добавление нового фильма
def add_movie(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение формы в базу данных
            return redirect('home')  # Перенаправление на главную страницу после добавления
    else:
        form = FilmForm()

    return render(request, 'films/add_movie.html', {'form': form})
