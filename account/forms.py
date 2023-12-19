from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class SignUP(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name']
