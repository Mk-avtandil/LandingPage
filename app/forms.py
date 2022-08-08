from logging import PlaceHolder
from django import forms

class SMTPForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Title'}))
    context = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Message'}))