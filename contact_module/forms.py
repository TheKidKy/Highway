from django import forms
from .models import Contact

class contact_form(forms.Form):
    subject = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=30, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(max_length=30, widget=forms.Textarea(attrs={'class': 'form-control'}))

class contact_model_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__' # ['subject', 'name', 'email', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject...'
            }),

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name...'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email...'
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your message...'
            })
        }

        error_messages = {
           'subject': {
               'required': 'subject field is required!'
           },
            'name': {
               'required': 'name field is required!'
           },
            'email': {
               'required': 'email field is required!'
           },
            'message': {
               'required': 'message field is required!'
           },
        }