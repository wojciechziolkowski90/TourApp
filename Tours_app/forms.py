from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        data = super().clean()
        self.user = authenticate(**data)
        if self.user is None:
            raise ValidationError("Podaj poprawne dane logowania")
        return data

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    re_password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('re_password'):
            raise ValidationError("Hasła muszą się zgadzać")
        return data


class EmailForm(forms.Form):
    odbiorca = forms.EmailField()
    imie= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tekst = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
