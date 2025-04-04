from django.db import models

# Create your models here.
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)
    promedio = models.DecimalField(max_digits=4, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    creditos = models.IntegerField()
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    paginas = models.IntegerField()

    def __str__(self):
        return self.titulo

class LibroCategoria(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='categorias_libros')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='libros_categorias')
    fecha_asignacion = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('libro', 'categoria')

    def __str__(self):
        return f"{self.libro.titulo} - {self.categoria.nombre}"