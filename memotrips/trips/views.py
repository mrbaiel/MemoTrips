from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Memory
from .forms import MemoryForm

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        memories = Memory.objects.filter(user=request.user)
        return render(request, 'trips/templates/index.html', {'memories': memories})
    return render(request, 'trips/templates/welcome.html')

@login_required
def add_memory(request):
    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save()
            return redirect('index')
    else:
        form = MemoryForm()
    return render(request, 'trips/templates/add_memory.html', {'form': form})