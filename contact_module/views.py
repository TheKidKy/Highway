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
    JsonResponse ({'success': 'Your message has sent successfully'})

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# class ContactUsView(View):
#     def get(self, request: HttpRequest):
#         contact_form = contact_model_form()
#         context = {'contact_form': contact_form}
#         return render(request, 'contact.html', context)

#     def post(self, request: HttpRequest):
#         contact_form = contact_model_form(request.POST)
#         if contact_form.is_valid():
#             context = {'contact_form': contact_form}
#         return render(request, 'contact.html', context)
