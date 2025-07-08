from django.db import models


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome.title()

class Postagem(models.Model):
    titulo = models.CharField(verbose_name="Titulo", max_length=255)
    corpo = models.TextField(verbose_name="Mensagem")
    criado_em = models.DateTimeField(verbose_name= "Criado em", auto_now_add=True)
    ultima_modificacao = models.DateTimeField(verbose_name="Ultima modificação", auto_now=True)
    categoria = models.ManyToManyField('Categoria', related_name='postagens')

class Comentario(models.Model):
    autor = models.CharField(verbose_name="Auto", max_length=60)
    corpo = models.TextField(verbose_name="Mensagem")
    criado_em = models.DateTimeField(verbose_name= "Criado em" ,auto_now_add=True)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.autor} em {self.postagem.titulo.title()}'



