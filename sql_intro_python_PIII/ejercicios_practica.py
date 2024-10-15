#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Ing.Jesús Matías González
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Ing.Jesús Matías González"
__email__ = "ingjesusmrgonzalez@gmail.com"
__version__ = "1.1"

import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('secundaria.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS estudiante;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE estudiante(
                [identificador] INTEGER PRIMARY KEY AUTOINCREMENT,
                [nombre] TEXT NOT NULL,
                [edad] INTEGER NOT NULL,
                [grado] INTEGER,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


def fill(identificador, nombre, edad, grado, tutor):
    # print('Completemos esta tablita!')
    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia INSERT.
    # Observar que hay campos como "grade" y "tutor" que no son obligatorios
    # en el schema creado, puede obivar en algunos casos completar esos campos

    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    values = [identificador, nombre, edad, grado, tutor]

    c.execute("""
        INSERT INTO estudiante (identificador, nombre, edad, grado, tutor)
        VALUES (?,?,?,?,?);""", values)

    conn.commit()
    conn.close()


def fetch():
    # print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # todas las filas con todas sus columnas
    # Utilizar fetchone para imprimir de una fila a la vez
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    print('Recorrer los datos ingresados')
    for row in c.execute('SELECT * FROM estudiante'):
        print(row)

    conn.close()

def search_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # id / name / age

    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    for row in c.execute("SELECT identificador, nombre, edad FROM estudiante where grado=?",(str(grade))):
        print(row)

    conn.close()
    
def insert(grade):
    print('Nuevos ingresos!')
    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria

    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    c.execute("""
        INSERT INTO estudiante (nombre, edad)
        VALUES (?,?);""", grade)

    conn.commit()
    conn.close()

def modify(id, name):
    print('Modificando la tabla')
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" pasado como parámetro

    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    rowcount = c.execute("UPDATE estudiante SET nombre =? WHERE identificador =?",
                         (name, id)).rowcount

    print('Filas actualizadas:', rowcount)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    create_schema()   # create and reset database (DB)
    fill(1, "Jesús González", 40, 1, "Madre")
    fill(2, "Rosa Chavez", 28, 1, "Madre")
    fill(3, "Carolina Figueroa", 24, 2, "Padre")
    fill(4, "Francisco Gallo", 23, 2, "Madre")
    fill(5, "Gastón Villarreal", 35, 3, "Padre")
    fetch()

    grade =3
    search_by_grade(grade)

    new_student = ['You', 16]
    insert(new_student)

    fetch()

    name = '¿Instituto Zuviría?'
    id = 2
    modify(id, name)
    
    fetch()


