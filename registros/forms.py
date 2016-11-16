# registros/forms.py

from django import forms

GENEROS = ("M", "F")
OPCIONES_ESTADO_CIVIL = ("S", "C", "V", "D")

class Dummy:
	genero = forms.MultipleChoiceField(
        required = True,
        widget   = forms.CheckboxSelectMultiple,
        choices  = GENEROS,
    )
    estado_civil = forms.MultipleChoiceField(
        required = True,
        widget   = forms.CheckboxSelectMultiple,
        choices  = OPCIONES_ESTADO_CIVIL,
    )     

