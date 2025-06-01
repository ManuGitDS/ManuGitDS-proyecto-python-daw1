import sqlite3

class Conexion():
    def __init__(self):
        try:
            self.con = sqlite3.connect("salines.db")
            self.creartablas()
            self.crearProfes()
            self.crearAlumnos()
            self.crearCursos()
            self.crearInscripciones()
        except Exception as ex:
            print("La base de datos ya existe",ex)

    # def creartablas(self):
    #     sql_create_table1 = """ CREATE TABLE IF NOT EXISTS profesores
    #     (id_profesor INTEGER PRIMARY KEY AUTOINCREMENT,
    #     nombre TEXT,
    #     primer_apellido TEXT,
    #     segundo_apellido TEXT,
    #     usuario TEXT UNIQUE,
    #     password TEXT)"""

    #     sql_create_table2 = """ CREATE TABLE IF NOT EXISTS alumnos
    #     (id_alumno INTEGER PRIMARY KEY AUTOINCREMENT,
    #     nombre TEXT,
    #     primer_apellido TEXT,
    #     segundo_apellido TEXT,
    #     usuario TEXT UNIQUE,
    #     password TEXT)"""
    #     cur = self.con.cursor()
    #     cur.execute(sql_create_table1)
    #     cur.execute(sql_create_table2)
    #     cur.close()
    #     self.crearProfes()
    #     self.crearAlumnos()


    # def crearProfes(self):
    #     try:
    #         sql_insert = """INSERT INTO profesores (id_profesor,nombre,primer_apellido,segundo_apellido,usuario,password)
    #         VALUES  
    #             (NULL,'Luis','Garcia','Gonzalez','luisi','1234'),
    #             (NULL,'Rafa','Garcia','Fillol','rafa','1234'),
    #             (NULL,'Antonio','Garcia','Gonzalez','toni','1234')
    #         """
    #         cur = self.con.cursor()
    #         cur.execute(sql_insert)
    #         cur.close()
    #         self.con.commit()
    #     except Exception as ex:
    #         print(ex)

    # def crearAlumnos(self):
    #     try:
    #         sql_insert = """INSERT INTO alumnos (id_alumno,nombre,primer_apellido,segundo_apellido,usuario,password)
    #         VALUES  (NULL,'noelia','Gonzalez','Cerezo','noeS','1234'),
    #             (NULL,'kiker','Gonzalez','Garcia','ikeron','1234'),
    #             (NULL,'Isabel','Lopez','Martin','isi','1234')
    #         """
    #         cur = self.con.cursor()
    #         cur.execute(sql_insert)
    #         cur.close()
    #         self.con.commit()
    #     except Exception as ex:
    #         print(ex)
    
    def creartablas(self):
        try:
            sql_create_table1 = """ CREATE TABLE IF NOT EXISTS profesores (
                id_profesor INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                primer_apellido TEXT,
                segundo_apellido TEXT,
                usuario TEXT UNIQUE,
                password TEXT
            )"""
            
            sql_create_table2 = """ CREATE TABLE IF NOT EXISTS alumnos (
                id_alumno INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                primer_apellido TEXT,
                segundo_apellido TEXT,
                usuario TEXT UNIQUE,
                password TEXT
            )"""
            
            sql_create_table3 = """ CREATE TABLE IF NOT EXISTS cursos (
                id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                descripcion TEXT,
                id_profesor INTEGER,
                FOREIGN KEY (id_profesor) REFERENCES profesores (id_profesor)
            )"""
            
            sql_create_table4 = """ CREATE TABLE IF NOT EXISTS inscripciones (
                id_inscripcion INTEGER PRIMARY KEY AUTOINCREMENT,
                id_alumno INTEGER,
                id_curso INTEGER,
                fecha_inscripcion DATE,
                FOREIGN KEY (id_alumno) REFERENCES alumnos (id_alumno),
                FOREIGN KEY (id_curso) REFERENCES cursos (id_curso)
            )"""
            
            cur = self.con.cursor()
            cur.execute(sql_create_table3)
            cur.execute(sql_create_table4)
            self.con.commit()
            cur.close()
            print("Tablas creadas correctamente.")
            

        except Exception as ex:
            print("Error al crear tablas:", ex)

    # def crearCursos(self):
    #     try:
    #         sql_insert = """INSERT INTO cursos (nombre, descripcion, id_profesor)
    #         VALUES  
    #             ('Matemáticas', 'Curso de matemáticas básicas', 1),
    #             ('Historia', 'Curso de historia moderna', 2),
    #             ('Inglés', 'Curso de inglés avanzado', 3),
    #             ('Biología', 'Curso de biología celular', 1),
    #             ('Arte', 'Curso de arte contemporáneo', 2),
    #             ('Literatura', 'Curso de literatura clásica', 3),
    #             ('Química', 'Curso de química orgánica', 1),
    #             ('Música', 'Curso de teoría musical', 2),
    #             ('Educación Física', 'Curso de deportes y salud', 3),
    #             ('Informática', 'Curso de programación básica', 1)
    #         """
    #         cur = self.con.cursor()
    #         cur.execute(sql_insert)
    #         self.con.commit()
    #         cur.close()
    #     except Exception as ex:
    #         print("Error al insertar cursos:", ex)

    # def crearInscripciones(self):
    #     try:
    #         sql_insert = """INSERT INTO inscripciones (id_alumno, id_curso, fecha_inscripcion)
    #         VALUES  
    #             (1, 1, '2024-05-20'),
    #             (2, 2, '2024-05-21'),
    #             (3, 3, '2024-05-22'),
    #             (4, 4, '2024-05-23'),
    #             (5, 5, '2024-05-24'),
    #             (6, 6, '2024-05-25'),
    #             (7, 7, '2024-05-26'),
    #             (8, 8, '2024-05-27'),
    #             (9, 9, '2024-05-28'),
    #             (10, 10, '2024-05-29')
    #         """
    #         cur = self.con.cursor()
    #         cur.execute(sql_insert)
    #         self.con.commit()
    #         cur.close()
    #     except Exception as ex:
    #         print("Error al insertar inscripciones:", ex)
    def conexion(self):
        return self.con
con = Conexion() 