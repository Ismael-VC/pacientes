from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

from registros.models import Paciente, Medicamento

class PacienteListView(ListView):

    model = Paciente

    def get_context_data(self, **kwargs):
        context = super(PacienteListView, self).get_context_data(**kwargs)
        return context



class PacienteDetailView(DetailView):

    model = Paciente

    def get_context_data(self, **kwargs):
        context = super(PacienteDetailView, self).get_context_data(**kwargs)
        return context