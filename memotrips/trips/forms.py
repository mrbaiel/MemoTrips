import form
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "comment", 'location']
        widgets = {
            'location': forms.HiddenInput(),
        }
        labels = {
            'title': "Названия",
            'comment': "Комментарий",
            'location': 'Место на карте',
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
