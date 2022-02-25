## Analizador léxico en consola
### Nombre desarrollador
Elías Abraham Vasquez Soto
### Carnet
201900131
### Sección
LABORATORIO LENGUAJES FORMALES Y DE PROGRAMACION Sección B-
### Descripción
Aplicación en consola, desarrollada en Python, que permite la lectura de un archivo de texto plano con extensión .lfp que contiene los datos de los estudiantes de un curso y la nota final que obtuvieron en dicho curso, además de palabras reservadas que indica que tipo de reporte se quiere realizar.

**Estructura del archivo:**
```
NOMBRE_DEL_CURSO = { 
< "Estudiante 01" ; 65 >,
< "Estudiante 02" ; 89 >,
< "Estudiante 03" ; 36 >,
< "Estudiante 04" ; 65 >,
< "Estudiante 05" ; 99 >,
< "Estudiante 06" ; 71 >
} PARAMETRO

```
**Parámetros que acepta:**
```
● ASC = Ordenar ascendentemente las notas de los estudiantes.
● DESC = Ordenar descendentemente las notas de los estudiantes.
● AVG = Obtener el promedio de los estudiantes del curso.
● MIN = Obtener la nota mínima de los estudiantes del curso.
● MAX = Obtener la nota máxima de los estudiantes del curso.
● APR = Obtener el número de estudiantes aprobados en el curso.
● REP = Obtener el número de estudiantes reprobados en el curso.
```
