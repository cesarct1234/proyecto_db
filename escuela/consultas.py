
from django.db.models import Q, F, Count, Avg, Sum, Min, Max
from .models import Estudiante, Curso, Libro, Categoria, LibroCategoria
import time
from datetime import datetime

# 1. Crear datos de prueba
def crear_datos_prueba():
    # Crear estudiantes
    estudiantes = [
        Estudiante(nombre="Ana", apellido="García", edad=20, email="ana@ejemplo.com", promedio=8.75),
        Estudiante(nombre="Carlos", apellido="Martínez", edad=22, email="carlos@ejemplo.com", promedio=9.30),
        Estudiante(nombre="Elena", apellido="López", edad=19, email="elena@ejemplo.com", promedio=7.80),
        Estudiante(nombre="Miguel", apellido="Rodríguez", edad=21, email="miguel@ejemplo.com", promedio=8.90),
        Estudiante(nombre="Laura", apellido="Fernández", edad=20, email="laura@ejemplo.com", promedio=9.50)
    ]
    
    for estudiante in estudiantes:
        estudiante.save()
    
    # Crear cursos
    cursos = [
        Curso(nombre="Programación Python", codigo="PY101", descripcion="Introducción a Python", creditos=4),
        Curso(nombre="Bases de Datos", codigo="DB201", descripcion="Fundamentos de bases de datos", creditos=5),
        Curso(nombre="Inteligencia Artificial", codigo="IA301", descripcion="Conceptos básicos de IA", creditos=6),
        Curso(nombre="Estructura de Datos", codigo="ED202", descripcion="Algoritmos y estructuras de datos", creditos=4),
        Curso(nombre="Desarrollo Web", codigo="WEB101", descripcion="Fundamentos de desarrollo web", creditos=3)
    ]
    
    for curso in cursos:
        curso.save()
    
    # Asignar estudiantes a cursos
    cursos[0].estudiantes.add(estudiantes[0], estudiantes[1], estudiantes[2])
    cursos[1].estudiantes.add(estudiantes[0], estudiantes[3], estudiantes[4])
    cursos[2].estudiantes.add(estudiantes[1], estudiantes[2])
    cursos[3].estudiantes.add(estudiantes[3], estudiantes[4])
    cursos[4].estudiantes.add(estudiantes[0], estudiantes[1], estudiantes[2], estudiantes[3], estudiantes[4])

    # Crear categorías
    categorias = [
        Categoria(nombre="Ciencia Ficción", descripcion="Libros de ciencia ficción"),
        Categoria(nombre="Programación", descripcion="Libros sobre programación"),
        Categoria(nombre="Historia", descripcion="Libros de historia"),
        Categoria(nombre="Fantasía", descripcion="Libros de fantasía"),
        Categoria(nombre="Educación", descripcion="Libros educativos")
    ]
    
    for categoria in categorias:
        categoria.save()
    
    # Crear libros
    libros = [
        Libro(titulo="El nombre del viento", autor="Patrick Rothfuss", fecha_publicacion=datetime.strptime("2007-03-27", "%Y-%m-%d").date(), isbn="1234567890123", paginas=662),
        Libro(titulo="Python Crash Course", autor="Eric Matthes", fecha_publicacion=datetime.strptime("2019-05-03", "%Y-%m-%d").date(), isbn="2345678901234", paginas=544),
        Libro(titulo="1984", autor="George Orwell", fecha_publicacion=datetime.strptime("1949-06-08", "%Y-%m-%d").date(), isbn="3456789012345", paginas=328),
        Libro(titulo="Dune", autor="Frank Herbert", fecha_publicacion=datetime.strptime("1965-08-01", "%Y-%m-%d").date(), isbn="4567890123456", paginas=412),
        Libro(titulo="Clean Code", autor="Robert C. Martin", fecha_publicacion=datetime.strptime("2008-08-01", "%Y-%m-%d").date(), isbn="5678901234567", paginas=464)
    ]
    
    for libro in libros:
        libro.save()
    
    # Asignar categorías a libros
    relaciones = [
        LibroCategoria(libro=libros[0], categoria=categorias[3]),
        LibroCategoria(libro=libros[1], categoria=categorias[1]),
        LibroCategoria(libro=libros[1], categoria=categorias[4]),
        LibroCategoria(libro=libros[2], categoria=categorias[0]),
        LibroCategoria(libro=libros[2], categoria=categorias[2]),
        LibroCategoria(libro=libros[3], categoria=categorias[0]),
        LibroCategoria(libro=libros[3], categoria=categorias[3]),
        LibroCategoria(libro=libros[4], categoria=categorias[1]),
        LibroCategoria(libro=libros[4], categoria=categorias[4])
    ]
    
    for relacion in relaciones:
        relacion.save()
    
    print("Datos de prueba creados exitosamente.")

# 2. Consultas básicas para Estudiantes
def consultas_basicas_estudiantes():
    print("CONSULTAS BÁSICAS PARA ESTUDIANTES:")
    
    # Obtener todos los estudiantes
    print("\nTodos los estudiantes:")
    estudiantes = Estudiante.objects.all()
    for estudiante in estudiantes:
        print(f"{estudiante.nombre} {estudiante.apellido} - {estudiante.email}")
    
    # Obtener un estudiante por ID
    print("\nEstudiante con ID 1:")
    try:
        estudiante = Estudiante.objects.get(id=1)
        print(f"{estudiante.nombre} {estudiante.apellido} - {estudiante.email}")
    except Estudiante.DoesNotExist:
        print("No se encontró el estudiante.")
    
    # Filtrar estudiantes por edad
    print("\nEstudiantes con edad >= 21:")
    estudiantes_mayores = Estudiante.objects.filter(edad__gte=21)
    for estudiante in estudiantes_mayores:
        print(f"{estudiante.nombre} {estudiante.apellido} - {estudiante.edad} años")
    
    # Ordenar estudiantes por promedio (descendente)
    print("\nEstudiantes ordenados por promedio (mayor a menor):")
    estudiantes_promedio = Estudiante.objects.order_by('-promedio')
    for estudiante in estudiantes_promedio:
        print(f"{estudiante.nombre} {estudiante.apellido} - Promedio: {estudiante.promedio}")
    
    # Conteo de estudiantes
    print(f"\nTotal de estudiantes: {Estudiante.objects.count()}")

# 3. Consultas básicas para Cursos
def consultas_basicas_cursos():
    print("CONSULTAS BÁSICAS PARA CURSOS:")
    
    # Obtener todos los cursos
    print("\nTodos los cursos:")
    cursos = Curso.objects.all()
    for curso in cursos:
        print(f"{curso.nombre} ({curso.codigo}) - {curso.creditos} créditos")
    
    # Obtener un curso por código
    print("\nCurso con código PY101:")
    try:
        curso = Curso.objects.get(codigo="PY101")
        print(f"{curso.nombre} - {curso.descripcion}")
    except Curso.DoesNotExist:
        print("No se encontró el curso.")
    
    # Filtrar cursos por créditos
    print("\nCursos con 4 o más créditos:")
    cursos_creditos = Curso.objects.filter(creditos__gte=4)
    for curso in cursos_creditos:
        print(f"{curso.nombre} - {curso.creditos} créditos")
    
    # Ordenar cursos por nombre
    print("\nCursos ordenados por nombre:")
    cursos_nombre = Curso.objects.order_by('nombre')
    for curso in cursos_nombre:
        print(f"{curso.nombre}")
    
    # Estudiantes en un curso específico
    print("\nEstudiantes en el curso 'Programación Python':")
    try:
        curso_python = Curso.objects.get(nombre="Programación Python")
        estudiantes = curso_python.estudiantes.all()
        for estudiante in estudiantes:
            print(f"{estudiante.nombre} {estudiante.apellido}")
    except Curso.DoesNotExist:
        print("No se encontró el curso.")
    
    # Cursos de un estudiante específico
    print("\nCursos del estudiante 'Ana García':")
    try:
        estudiante_ana = Estudiante.objects.get(nombre="Ana", apellido="García")
        cursos = estudiante_ana.cursos.all()
        for curso in cursos:
            print(f"{curso.nombre} ({curso.codigo})")
    except Estudiante.DoesNotExist:
        print("No se encontró el estudiante.")

# Parte 1: Consultas avanzadas con Q, F y filtrados de texto
def consultas_avanzadas():
    print("CONSULTAS AVANZADAS CON Q, F Y FILTRADOS DE TEXTO:")
    
    # Consultas con Q (operaciones lógicas complejas)
    print("\nEstudiantes con edad > 20 Y promedio > 9.0 O con apellido 'García':")
    consulta_q = Estudiante.objects.filter(
        (Q(edad__gt=20) & Q(promedio__gt=9.0)) | Q(apellido='García')
    )
    for estudiante in consulta_q:
        print(f"{estudiante.nombre} {estudiante.apellido} - Edad: {estudiante.edad}, Promedio: {estudiante.promedio}")
    
    # Consultas con F (operaciones entre campos)
    print("\nCursos donde el número de créditos es mayor que la longitud del código:")
    consulta_f = Curso.objects.filter(creditos__gt=F('codigo').length())
    for curso in consulta_f:
        print(f"{curso.nombre} - Créditos: {curso.creditos}, Código: {curso.codigo} (longitud: {len(curso.codigo)})")
    
    # Incrementar la edad de todos los estudiantes en 1
    print("\nIncrementar la edad de todos los estudiantes en 1:")
    Estudiante.objects.update(edad=F('edad') + 1)
    for estudiante in Estudiante.objects.all():
        print(f"{estudiante.nombre} {estudiante.apellido} - Nueva edad: {estudiante.edad}")
    
    # Filtrados de texto
    print("\nEstudiantes cuyo nombre contiene 'a':")
    consulta_texto = Estudiante.objects.filter(nombre__contains='a')
    for estudiante in consulta_texto:
        print(f"{estudiante.nombre} {estudiante.apellido}")
    
    print("\nCursos que empiezan con 'P':")
    consulta_texto = Curso.objects.filter(nombre__startswith='P')
    for curso in consulta_texto:
        print(f"{curso.nombre}")
    
    print("\nCursos que terminan con 'n':")
    consulta_texto = Curso.objects.filter(nombre__endswith='n')
    for curso in consulta_texto:
        print(f"{curso.nombre}")
    
    print("\nBúsqueda case-insensitive de cursos que contienen 'dat':")
    consulta_texto = Curso.objects.filter(nombre__icontains='dat')
    for curso in consulta_texto:
        print(f"{curso.nombre}")
    
    # Consultas con negación
    print("\nEstudiantes que NO tienen apellido 'García':")
    consulta_negacion = Estudiante.objects.exclude(apellido='García')
    for estudiante in consulta_negacion:
        print(f"{estudiante.nombre} {estudiante.apellido}")
    
    # Consultas con agregación
    print("\nPromedio de edad de los estudiantes:")
    promedio_edad = Estudiante.objects.aggregate(promedio_edad=Avg('edad'))
    print(f"Promedio de edad: {promedio_edad['promedio_edad']}")
    
    print("\nCréditos totales de todos los cursos:")
    suma_creditos = Curso.objects.aggregate(total_creditos=Sum('creditos'))
    print(f"Total de créditos: {suma_creditos['total_creditos']}")
    
    print("\nCursos con su número de estudiantes:")
    cursos_conteo = Curso.objects.annotate(num_estudiantes=Count('estudiantes'))
    for curso in cursos_conteo:
        print(f"{curso.nombre} - {curso.num_estudiantes} estudiantes")

# Parte 2: Consultas sobre la relación muchos a muchos entre Libro y Categoria
def consultas_muchos_a_muchos():
    print("CONSULTAS SOBRE LA RELACIÓN MUCHOS A MUCHOS ENTRE LIBRO Y CATEGORIA:")
    
    # Libros de una categoría específica
    print("\nLibros de la categoría 'Programación':")
    try:
        categoria_prog = Categoria.objects.get(nombre='Programación')
        libros_prog = Libro.objects.filter(categorias_libros__categoria=categoria_prog)
        for libro in libros_prog:
            print(f"{libro.titulo} - {libro.autor}")
    except Categoria.DoesNotExist:
        print("No se encontró la categoría.")
    
    # Categorías de un libro específico
    print("\nCategorías del libro 'Python Crash Course':")
    try:
        libro_python = Libro.objects.get(titulo='Python Crash Course')
        categorias_libro = Categoria.objects.filter(libros_categorias__libro=libro_python)
        for categoria in categorias_libro:
            print(f"{categoria.nombre}")
    except Libro.DoesNotExist:
        print("No se encontró el libro.")
    
    # Libros con múltiples categorías
    print("\nLibros que pertenecen a más de una categoría:")
    libros_multi = Libro.objects.annotate(num_categorias=Count('categorias_libros')).filter(num_categorias__gt=1)
    for libro in libros_multi:
        categorias = Categoria.objects.filter(libros_categorias__libro=libro)
        categorias_nombres = [cat.nombre for cat in categorias]
        print(f"{libro.titulo} - Categorías: {', '.join(categorias_nombres)}")
    
    # Libros sin categoría
    print("\nLibros sin categoría asignada:")
    libros_sin_cat = Libro.objects.annotate(num_categorias=Count('categorias_libros')).filter(num_categorias=0)
    for libro in libros_sin_cat:
        print(f"{libro.titulo}")
    
    # Categorías sin libros
    print("\nCategorías sin libros asignados:")
    cat_sin_libros = Categoria.objects.annotate(num_libros=Count('libros_categorias')).filter(num_libros=0)
    for categoria in cat_sin_libros:
        print(f"{categoria.nombre}")
    
    # Categoría con más libros
    print("\nCategoría con más libros:")
    cat_mas_libros = Categoria.objects.annotate(num_libros=Count('libros_categorias')).order_by('-num_libros').first()
    if cat_mas_libros:
        print(f"{cat_mas_libros.nombre} - {cat_mas_libros.num_libros} libros")
    
    # Libro con más categorías
    print("\nLibro con más categorías:")
    libro_mas_cat = Libro.objects.annotate(num_categorias=Count('categorias_libros')).order_by('-num_categorias').first()
    if libro_mas_cat:
        print(f"{libro_mas_cat.titulo} - {libro_mas_cat.num_categorias} categorías")

# Parte 3: Optimización de consultas
def optimizar_consultas():
    print("OPTIMIZACIÓN DE CONSULTAS:")
    
    # Usando select_related para relaciones ForeignKey
    print("\nUsando select_related:")
    print("Libros y sus categorías (sin select_related):")
    import time
    
    start_time = time.time()
    relaciones = LibroCategoria.objects.all()[:5]
    for relacion in relaciones:
        print(f"{relacion.libro.titulo} - {relacion.categoria.nombre}")
    print(f"Tiempo sin select_related: {time.time() - start_time:.6f} segundos")
    
    start_time = time.time()
    relaciones = LibroCategoria.objects.select_related('libro', 'categoria')[:5]
    for relacion in relaciones:
        print(f"{relacion.libro.titulo} - {relacion.categoria.nombre}")
    print(f"Tiempo con select_related: {time.time() - start_time:.6f} segundos")
    
    # Usando prefetch_related para relaciones ManyToMany
    print("\nUsando prefetch_related:")
    print("Cursos y sus estudiantes (sin prefetch_related):")
    
    start_time = time.time()
    cursos = Curso.objects.all()[:3]
    for curso in cursos:
        print(f"{curso.nombre} - Estudiantes: {', '.join([e.nombre for e in curso.estudiantes.all()])}")
    print(f"Tiempo sin prefetch_related: {time.time() - start_time:.6f} segundos")
    
    start_time = time.time()
    cursos = Curso.objects.prefetch_related('estudiantes')[:3]
    for curso in cursos:
        print(f"{curso.nombre} - Estudiantes: {', '.join([e.nombre for e in curso.estudiantes.all()])}")
    print(f"Tiempo con prefetch_related: {time.time() - start_time:.6f} segundos")
    
    # Usando only() para recuperar solo los campos necesarios
    print("\nUsando only():")
    print("Nombres y apellidos de estudiantes (sin only):")
    
    start_time = time.time()
    estudiantes = Estudiante.objects.all()[:5]
    for estudiante in estudiantes:
        print(f"{estudiante.nombre} {estudiante.apellido}")
    print(f"Tiempo sin only: {time.time() - start_time:.6f} segundos")
    
    start_time = time.time()
    estudiantes = Estudiante.objects.only('nombre', 'apellido')[:5]
    for estudiante in estudiantes:
        print(f"{estudiante.nombre} {estudiante.apellido}")
    print(f"Tiempo con only: {time.time() - start_time:.6f} segundos")
    
    # Usando defer() para excluir campos que no se utilizarán
    print("\nUsando defer():")
    print("Información básica de libros (sin defer):")
    
    start_time = time.time()
    libros = Libro.objects.all()[:5]
    for libro in libros:
        print(f"{libro.titulo} - {libro.autor}")
    print(f"Tiempo sin defer: {time.time() - start_time:.6f} segundos")
    
    start_time = time.time()
    libros = Libro.objects.defer('fecha_publicacion', 'isbn', 'paginas')[:5]
    for libro in libros:
        print(f"{libro.titulo} - {libro.autor}")
    print(f"Tiempo con defer: {time.time() - start_time:.6f} segundos")
    
    # Combinando técnicas de optimización
    print("\nCombinando técnicas de optimización:")
    
    start_time = time.time()
    cursos = Curso.objects.prefetch_related('estudiantes').only('nombre', 'codigo')[:3]
    for curso in cursos:
        print(f"{curso.nombre} ({curso.codigo}) - Estudiantes: {', '.join([e.nombre for e in curso.estudiantes.only('nombre')])}")
    print(f"Tiempo con optimización combinada: {time.time() - start_time:.6f} segundos")

# Función principal para ejecutar todas las consultas
def ejecutar_consultas():
    # Primero creamos los datos de prueba
    crear_datos_prueba()
    
    # Luego ejecutamos las consultas
    consultas_basicas_estudiantes()
    print("\n" + "-"*50 + "\n")
    
    consultas_basicas_cursos()
    print("\n" + "-"*50 + "\n")
    
    consultas_avanzadas()
    print("\n" + "-"*50 + "\n")
    
    consultas_muchos_a_muchos()
    print("\n" + "-"*50 + "\n")
    
    optimizar_consultas()