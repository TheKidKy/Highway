from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import View
from .forms import contact_model_form
from django.http import JsonResponse, HttpRequest

# Create your views here.

class ContactUsView(FormView):
    template_name = 'contact.html'
    form_class = contact_model_form
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

