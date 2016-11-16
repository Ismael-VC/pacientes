from django.conf.urls import url

from registros.views import PacienteListView, PacienteDetailView

urlpatterns = [
    url(r'^$', PacienteListView.as_view(), name='pacientes-lista'),
    url(r'^(?P<slug>[-\w]+)/$', PacienteDetailView.as_view(), name='paciente-detail'),
]



