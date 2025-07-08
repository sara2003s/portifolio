from django.contrib import admin
from .models import Postagem, Categoria, Comentario

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'criado_em', 'listar_categorias')

    def listar_categorias(self, obj):
        return ", ".join([categoria.nome for categoria in obj.categoria.all()])
    listar_categorias.short_description = 'Categorias'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass

