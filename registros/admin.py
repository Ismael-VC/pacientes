from django.contrib import admin

# Register your models here.

from .models import Paciente, Medicamento



class PacienteAdmin(admin.ModelAdmin):
    model = Paciente
    search_fields = ('id', 'nombre')
    readonly_fields=('id',)
    list_display = ['id', 'nombre']

#admin.site.unregister(Paciente)
admin.site.register(Paciente, PacienteAdmin)
