from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(user=request.user)
        return render(request, 'index.html', {'notes': notes})
    return render(request, 'welcome.html')


@login_required
def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})


def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('index')
    return render(request, 'confirm_delete_note.html', {'note':note})
