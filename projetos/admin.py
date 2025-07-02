from django.contrib import admin
from projetos.models import Projeto

# Register your models here.
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo_alias', 'descricao_alias', 'tecnologias_alias')
    list_filter = ('tecnologias',)
    ordering = ('tecnologias',)
    search_fields = ('titulo',)

    @admin.display(description='Título')
    def titulo_alias(self, obj):
        return obj.titulo.title()
    
    @admin.display(description='Descrição')
    def descricao_alias(self, obj):   
        return obj.descricao.title()
    
    @admin.display(description='Tecnologias')
    def tecnologias_alias(self, obj):  
        return obj.tecnologias.title()

