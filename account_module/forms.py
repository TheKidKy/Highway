from django import forms
from django.forms import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget = forms.TextInput(
            attrs={'placeholder': 'Username', 'class': 'input100'}
        ),
        error_messages={'required': 'username field is required!'}
    )

    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password', 'class': 'input100'}
        ),
        error_messages={'required': 'password field is required!'}
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget = forms.TextInput(
            attrs={'placeholder': 'Username', 'class': 'input100'}
        ),
        error_messages={'required': 'username field is required!'}
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email', 'class': 'input100'}
        ),
        error_messages={'required': 'email field is required!'}
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password', 'class': 'input100'}
        ),
        error_messages={'required': 'password field is required!'}
    )

    confirm_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm Password', 'class': 'input100'}
        )
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('The value of password and password confirm are not the same!')