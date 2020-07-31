from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


class TodoForms(forms.Form):
    description = forms.CharField(max_length=3000, required=True, label='Описание', widget=forms.Textarea)
    date = forms.DateField(label='Дата')
    detailed_description = forms.CharField(max_length=5000, required=False,  label='Подробное описание', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label="Статус", initial=default_status)