from django import forms
from django.core.exceptions import ValidationError

from users.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    full_name = forms.CharField(required=True, label='Name')
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput())

    def clean_username(self):
        value = self.cleaned_data['username']
        if User.objects.filter(username=value).count():
            raise ValidationError('Username taken')
        return value

    def clean_email(self):
        value = self.cleaned_data['email']
        if User.objects.filter(email=value).count():
            raise ValidationError('Email in use')
        return value

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            self.add_error('password', '')
            self.add_error('confirm_password', '')
            raise ValidationError('Passwords do not match')
