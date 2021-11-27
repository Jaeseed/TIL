from django.db import models
from .models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class SignUpForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['email', 'name','username', 'password']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': '휴대폰 번호 또는 이메일 주소'}),
            'name': forms.TextInput(attrs={'placeholder': '성명'}),
            'username': forms.TextInput(attrs={'placeholder': '사용자 이름'}),
            'password': forms.PasswordInput(attrs={'placeholder': '비밀번호'})
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class LogInForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': '사용자 이름'}),
            'password': forms.PasswordInput(attrs={'placeholder': '비밀번호'})
        }


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ['profile_photo', 'name', 'bio', 'email', 'phone_number', 'gender',]
