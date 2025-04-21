# GES - Gestión Educativa Simple

**GES** es un sistema básico de gestión educativa desarrollado con Python, pensado para centros educativos que necesitan una solución accesible, funcional y adaptada a su realidad. Diseñado especialmente para contextos con recursos limitados, GES busca digitalizar la administración académica sin complicaciones.

## ¿Por qué GES?

En muchos centros educativos se usa Excel para registrar estudiantes, profesores, notas y asistencia. GES no intenta reemplazar esa costumbre, sino **complementarla y mejorarla**, permitiendo importar/exportar desde archivos Excel y generar estadísticas útiles a partir de esos datos.

## Características principales

- Registro y gestión de estudiantes y profesores.
- Lista de asignaturas y vinculación a usuarios.
- Importación y exportación de datos en Excel.
- Generación de gráficas de rendimiento académico.
- Reportes básicos y análisis estadístico.

## Tecnologías utilizadas

- Python 3
- SQLite (base de datos local)
- Pandas + OpenPyXL (trabajo con Excel)
- Matplotlib (visualización de datos)
- Tkinter (interfaz gráfica, próximamente)

## Requisitos

Asegúrate de tener instalado Python 3. Luego, instala las dependencias:

```bash
pip install pandas openpyxl matplotlib
