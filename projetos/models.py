from django.db import models

# Create your models here.
class Projeto(models.Model):
    titulo = models.CharField(max_length=100) 
    descricao = models.TextField() 
    tecnologias = models.CharField(max_length=20)
    imagem = models.FileField(upload_to='imagens_projetos', blank=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo.title()
    