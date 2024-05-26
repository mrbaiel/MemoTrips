from django import forms
from .models import Memory

class MemoryForm(form.ModelForm):
    class Meta:
        model = Memory
        fields = ["title", "description", 'location']