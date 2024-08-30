from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Curso, Interesse, SobreMim

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_conclusao')

@admin.register(Interesse)
class InteresseAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(SobreMim)
class SobreMimAdmin(admin.ModelAdmin):
    list_display = ('biografia',)
