from django.contrib import admin
from app.models import Empresa, Cargo, Funcionario, Produto

class Empresas(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
admin.site.register(Empresa, Empresas)

class Funcionarios(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
admin.site.register(Funcionario, Funcionarios)

class Cargos(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
admin.site.register(Cargo, Cargos)

class Produtos(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
admin.site.register(Produto, Produtos)
# Register your models here.
