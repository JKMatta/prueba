from django import forms
from .models import Post
from .models import AdoptarRescatado

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'raza')


class AdopForm(forms.ModelForm):

	class Meta:
		model = AdoptarRescatado
		fields = ('rut', 'nombre', 'apellido')
		