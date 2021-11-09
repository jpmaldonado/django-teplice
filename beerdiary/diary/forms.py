from django import forms
from django.forms import widgets
from .models import Beer, Entry

class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ['name']
        labels = {'name':'Enter a beer name'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'beer']        
        labels = {'text':'Entry: '}
        widgets = {'text':forms.Textarea()}