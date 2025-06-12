from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 mt-2 border border-gray-300 rounded',
            'placeholder': 'Enter password'
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 mt-2 border border-gray-300 rounded',
            'placeholder': 'Confirm password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 mt-2 border border-gray-300 rounded',
                'placeholder': 'Enter username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 mt-2 border border-gray-300 rounded',
                'placeholder': 'Enter email'
            }),
            # 'role': forms.Select(attrs={
            #     'class': 'w-full px-4 py-2 mt-2 border border-gray-300 rounded'
            # }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")



class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Enter your email",
            }
        ),
        label="Email",
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Enter your password",
            }
        ),
        label="Password",
    )
