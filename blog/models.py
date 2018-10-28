from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    raza = models.CharField(max_length=80)
    text = models.TextField()
    imagen = models.FileField(null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        

    
class AdoptarRescatado(models.Model):
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    edad = models.IntegerField()
    celular = models.IntegerField()
    region = models.CharField(max_length=25)
    comuna = models.CharField(max_length=25)
    tipo_casa = models.CharField(max_length=25)
    nombre_rescatado = models.CharField(max_length=25)
    correo = models.CharField(max_length=50)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.rut

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text