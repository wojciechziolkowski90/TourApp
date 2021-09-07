from django import forms
from django.contrib.auth import authenticate
from jsonschema import ValidationError

from Tours_app.models import Tour


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)


    def clean(self):
        data = super().clean()
        self.user = authenticate(**data)
        if self.user is None:
            raise ValidationError("nie poprawne dane logowania")
        return data


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=60, widget=forms.PasswordInput, label="Re- pass")

    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('re_password'):
            raise ValidationError("hasła się nie zgadzają")
        return data


class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    user_review = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))