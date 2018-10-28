from django import forms
from .models import Post, Comment
from .models import AdoptarRescatado

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'raza')


class AdopForm(forms.ModelForm):

	class Meta:
		model = AdoptarRescatado
		fields = ('rut', 'nombre', 'apellido')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
		