import sqlite3

class BaseDeDatos:
    def __init__(self, db_name='ges_db.db'):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)
        
    def crear_tabla_aluno(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTs estudiantes (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        apellido TEXT,
                        curso TEXT,
                        clase TEXT,
                        turno TEXT,
                        centro TEXT,
                        tutor TEXT,
                        tell TEXT,
                        direccion TEXT,
                        calendario TEXT,
                        matricula INTEGER,
                        fecha TEXT)
                        ''')
        conexion.commit()
        conexion.close()
        
    def agregar_alumno(self, nombre, apellido, curso, clase, turno, centro, tutor, tell, direccion, calendario, matricula, fecha):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute('''INSERT INTO estudiantes(nombre, apellido, curso, clase, turno, centro,
                       tutor, tell, direccion, calendario, matricula, fecha) 
                       values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        conexion.commit()
        conexion.close()
        
    def obtener_alumnos(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM estudiantes')
        estudiantes = cursor.fetchall()
        conexion.close()
        return estudiantes
    
    def treeview_alumnos(self, ocultar_campos=None):
        conexion = self.connectar()
        cursor = conexion.cursor()
        cursor.execute('PRAGMA table_info(estudiantes)')
        columnas_info = cursor.fetchall()

        columnas = [col[1] for col in columnas_info]
        if ocultar_campos:
            columnas_visibles = [col for col in columnas if col not in ocultar_campos]
        else:
            columnas_visibles = columnas

        cursor.execute('SELECT * FROM estudiantes')
        filas = cursor.fetchall()
        filas_filtradas = [
            [valor for i, valor in enumerate(fila) if columnas[i] in columnas_visibles]
            for fila in filas
        ]

        conexion.close()
        return columnas_visibles, filas_filtradas
