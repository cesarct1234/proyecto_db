from django.contrib import admin
from .models import Estudiante, Curso, Libro, Categoria, LibroCategoria

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Libro)
admin.site.register(Categoria)
admin.site.register(LibroCategoria)