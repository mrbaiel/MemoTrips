# trips/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Note
from .forms import NoteForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def logout_view(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('login')


@login_required
def index(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_time')
    return render(request, 'index.html', {'notes': notes})


def welcome(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'welcome.html')


@login_required
def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, "Воспоминание успешно добавлено!")
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                print(f"Error in {field}: {errors}")
            messages.error(request, "Ошибка в форме. Пожалуйста, проверьте данные.")
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form})


@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'note': note})


@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('index')
    return render(request, 'confirm_delete_note.html', {'note': note})
