from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "name")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "name", "is_active", "is_staff", "is_verified")
