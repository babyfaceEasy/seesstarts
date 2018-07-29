from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from details.models import BioData

# Create your views here.

class LandingPage(View):
    def get(self, request):
        return render(request, 'details/index.html', {})
class BioDataCreate(SuccessMessageMixin, CreateView):
    template_name = 'details/biodata_create.html'
    model = BioData
    fields = ('name', 'email_address')
    success_url = reverse_lazy('biodata-list')
    success_message = "New user data creation was successful!"

class BioDataList(ListView):
    template_name = 'details/biodata_list.html'
    model = BioData