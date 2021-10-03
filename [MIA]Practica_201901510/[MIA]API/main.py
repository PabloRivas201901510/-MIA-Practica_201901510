from flask import Flask, redirect, url_for, render_template, request
import psycopg2
import os
app = Flask(__name__)

@app.route("/")
def home():
    tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
    tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
    tmp += '<main role="main" class="container p-5">'
    tmp += '<div class="p-5 bg-light border  rounded-3">'
    tmp += '<h1>PRACTICA 1</h1>'
    tmp += '<p>Manejo e Implementacion de Archivos</p>'
    tmp += '<small class="text-primary">Por Pablo Daniel Rivas Marroquin</small>'
    tmp += '</div>'
    tmp += '</main>'
    return tmp

# CONSULTA 1
@app.route("/consulta1")
def comando1():
    conn=None
    prints= [None]
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./consultas/consulta1.sql","r").read())
        prints = cur.fetchall()
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>CONSULTA  1</h1> <br>"
            tmp += "Cantidad de copias que existen en el inventario para la película “Sugar Wonka” <br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            return tmp+str(prints[0][0])

# CONSULTA 2
@app.route("/consulta2")
def comando2():
    conn=None
    prints= [None]
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./consultas/consulta2.sql","r").read())
        prints = cur.fetchall()
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>CONSULTA  2</h1> <br>"
            tmp += "nombre, apellido y pago total de todos los clientes que han rentado películas por lo menos 40 veces. <br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tabla = '<TABLE BORDER CELLPADDING=8 CELLSPACING=0>\n'
            tabla += '<TR><TH>No</TH><TH>Nombre_Cliente -</TH><TH>Apellido_Cliente</TH><TH>Pago_Total</TH></TR>'
            contador = 0
            for i in prints:
                contador += 1
                tabla += "<TR>"
                tabla += "<TD>"+str(contador)+"</TD>"
                for j in i:
                    tabla += "<TD>"+str(j)+"</TD>"
                tabla += "</TR>"
            tabla += "</TABLE>"
            return tmp+ tabla

# CONSULTA 3
@app.route("/consulta3")
def comando3():
    conn=None
    prints= [None]
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./consultas/consulta3.sql","r").read())
        prints = cur.fetchall()
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>CONSULTA  3</h1> <br>"
            tmp += "nombre y apellido (en una sola columna) de los actores que contienen la palabra “SON” en su apellido, ordenados por su primer nombre. <br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tabla = '<TABLE BORDER CELLPADDING=8 CELLSPACING=0>\n'
            tabla += '<TR><TH>No</TH><TH>Nombre_Apellido_Actor</TH></TR>'
            contador = 0
            for i in prints:
                contador += 1
                tabla += "<TR>"
                tabla += "<TD>"+str(contador)+"</TD>"
                for j in i:
                    tabla += "<TD>"+str(j)+"</TD>"
                tabla += "</TR>"
            tabla += "</TABLE>"
            return tmp+ tabla

# CONSULTA 4
@app.route("/consulta4")
def comando4():
    conn=None
    prints= [None]
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./consultas/consulta4.sql","r").read())
        prints = cur.fetchall()
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>CONSULTA  4</h1> <br>"
            tmp += "nombre y apellido de los actores que participaron en una película cuya descripción incluye la palabra “crocodile” y “shark” junto con el año de lanzamiento de la película, ordenados por el apellido del actor en forma ascendente. <br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tabla = '<TABLE BORDER CELLPADDING=8 CELLSPACING=0>\n'
            tabla += '<TR><TH>No</TH><TH>Nombre Actor</TH><TH>Apellido Actor</TH><TH>Año de Lanzamiento</TH></TR>'
            contador = 0
            for i in prints:
                contador += 1
                tabla += "<TR>"
                tabla += "<TD>"+str(contador)+"</TD>"
                for j in i:
                    tabla += "<TD>"+str(j)+"</TD>"
                tabla += "</TR>"
            tabla += "</TABLE>"
            return tmp+ tabla


# CONSULTA 5
@app.route("/consulta5")
def comando5():
    conn=None
    prints= [None]
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./consultas/consulta5.sql","r").read())
        prints = cur.fetchall()
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>CONSULTA  5</h1> <br>"
            tmp += "país y el nombre del cliente que más películas rentó así como también el porcentaje que representa la cantidad de películas que rentó conrespecto al resto de clientes del país. <br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tabla = '<TABLE BORDER CELLPADDING=8 CELLSPACING=0>\n'
            tabla += '<TR><TH>No</TH><TH>Pais Cliente</TH><TH>Nombre Cliente</TH><TH>Peliculas Rentadas</TH><TH>Peliculas Rentadas por Pais</TH><TH>Porcentaje %</TH></TR>'
            contador = 0
            for i in prints:
                contador += 1
                tabla += "<TR>"
                tabla += "<TD>"+str(contador)+"</TD>"
                for j in i:
                    tabla += "<TD>"+str(j)+"</TD>"
                tabla += "</TR>"
            tabla += "</TABLE>"
            return tmp+ tabla

# CONSULTA 6
@app.route("/consulta6")
def comando6():
    conn=None
    prints= [None]
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./consultas/consulta6.sql","r").read())
        prints = cur.fetchall()
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>CONSULTA  6</h1> <br>"
            tmp += "total de clientes y porcentaje de clientes por ciudad y país. El ciento por ciento es el total de clientes por país.<br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tabla = '<TABLE BORDER CELLPADDING=8 CELLSPACING=0>\n'
            tabla += '<TR><TH>No</TH><TH>Pais</TH><TH>Ciudad</TH><TH>Clientes por Ciudad</TH><TH>Clientes por Pais</TH><TH>Porcentaje %</TH></TR>'
            contador = 0
            for i in prints:
                contador += 1
                tabla += "<TR>"
                tabla += "<TD>"+str(contador)+"</TD>"
                for j in i:
                    tabla += "<TD>"+str(j)+"</TD>"
                tabla += "</TR>"
            tabla += "</TABLE>"
            return tmp+ tabla

# CONSULTA 7
@app.route("/consulta7")
def comando7():
    conn=None
    prints= [None]
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./consultas/consulta7.sql","r").read())
        prints = cur.fetchall()
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>CONSULTA  7</h1> <br>"
            tmp += "nombre del país, la ciudad y el promedio de rentas por ciudad.<br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tabla = '<TABLE BORDER CELLPADDING=8 CELLSPACING=0>\n'
            tabla += '<TR><TH>No</TH><TH>Pais</TH><TH>Ciudad</TH><TH>Rentas por Ciudad</TH><TH>Ciudades por Pais</TH><TH>Promedio</TH></TR>'
            contador = 0
            for i in prints:
                contador += 1
                tabla += "<TR>"
                tabla += "<TD>"+str(contador)+"</TD>"
                for j in i:
                    tabla += "<TD>"+str(j)+"</TD>"
                tabla += "</TR>"
            tabla += "</TABLE>"
            return tmp+ tabla

# CONSULTA 8
@app.route("/consulta8")
def comando8():
    conn=None
    prints= [None]
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./consultas/consulta8.sql","r").read())
        prints = cur.fetchall()
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>CONSULTA  8</h1> <br>"
            tmp += "nombre del país y el porcentaje de rentas de películas de la categoría “Sports”.<br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tabla = '<TABLE BORDER CELLPADDING=8 CELLSPACING=0>\n'
            tabla += '<TR><TH>No</TH><TH>Pais</TH><TH>Rentas Categoria Sports</TH><TH>Rentas por Pais</TH><TH>Porcentaje %</TH></TR>'
            contador = 0
            for i in prints:
                contador += 1
                tabla += "<TR>"
                tabla += "<TD>"+str(contador)+"</TD>"
                for j in i:
                    tabla += "<TD>"+str(j)+"</TD>"
                tabla += "</TR>"
            tabla += "</TABLE>"
            return tmp+ tabla

# CONSULTA 9
@app.route("/consulta9")
def comando9():
    conn=None
    prints= [None]
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./consultas/consulta9.sql","r").read())
        prints = cur.fetchall()
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>CONSULTA  9</h1> <br>"
            tmp += "lista de ciudades de Estados Unidos y el número de rentas de películas para las ciudades que obtuvieron más rentas que la ciudad “Dayton”.<br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tabla = '<TABLE BORDER CELLPADDING=8 CELLSPACING=0>\n'
            tabla += '<TR><TH>No</TH><TH>Pais</TH><TH>Ciudad</TH><TH>Rentas por Ciudad</TH></TR>'
            contador = 0
            for i in prints:
                contador += 1
                tabla += "<TR>"
                tabla += "<TD>"+str(contador)+"</TD>"
                for j in i:
                    tabla += "<TD>"+str(j)+"</TD>"
                tabla += "</TR>"
            tabla += "</TABLE>"
            return tmp+ tabla

# CONSULTA 10
@app.route("/consulta10")
def comando10():
    conn=None
    prints= [None]
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./consultas/consulta10.sql","r").read())
        prints = cur.fetchall()
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>CONSULTA  10</h1> <br>"
            tmp += "ciudades por país en las que predomina la renta de películas de la categoría “Horror”. <br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tabla = '<TABLE BORDER CELLPADDING=8 CELLSPACING=0>\n'
            tabla += '<TR><TH>No</TH><TH>Pais</TH><TH>Ciudad</TH><TH>Rentas Categoria Horror</TH></TR>'
            contador = 0
            for i in prints:
                contador += 1
                tabla += "<TR>"
                tabla += "<TD>"+str(contador)+"</TD>"
                for j in i:
                    tabla += "<TD>"+str(j)+"</TD>"
                tabla += "</TR>"
            tabla += "</TABLE>"
            return tmp+ tabla

# cargarTemporal
@app.route("/cargarTemporal")
def cargarTemporal():
    conn=None
    text = "COPY temporal FROM '"+str(os.getcwd()+"/data/BlockbusterData.csv")+"' (FORMAT 'csv', DELIMITER ';', NULL '-', HEADER 'true');"
    try:
        #print(str(os.getcwd()+"/data/BlockbusterData.csv"))
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(text)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>CARGA TEMPORAL</h1> <br>"
            tmp += "Carga masiva de datos a tabla temporal <br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tmp += 'Datos a Temporal Cargados.'
            return tmp

# cargarModelo
@app.route("/cargarModelo")
def cargarModelo():
    conn=None
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./sentencias/cargarModelo.sql","r").read())
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>CARGAR MODELO</h1> <br>"
            tmp += "Crear tablas del modelo y cargarle los datos <br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tmp += 'Tablas y Datos Cargados.'
            return tmp

# eliminarTemporal
@app.route("/eliminarTemporal")
def eliminarTemporal():
    conn=None
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./sentencias/eliminarTemporal.sql","r").read())
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>ELIMINAR TEMPORAL</h1> <br>"
            tmp += "Eliminar datos de la tabla temporal <br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tmp += 'Datos de la tabla temporal eliminados.'
            return tmp

# eliminarModelo
@app.route("/eliminarModelo")
def eliminarModelo():
    conn=None
    try:
        conn = psycopg2.connect(host="localhost",database="blockbuster",user="postgres")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(open("./sentencias/eliminarModelo.sql","r").read())
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            tmp = '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/cyborg/bootstrap.css">'
            tmp += '<link rel="stylesheet" type="text/css" href="https://bootswatch.com/_assets/css/custom.min.css">'
            tmp += '<main role="main" class="container p-5">'
            tmp += '<div class="p-5 bg-light border  rounded-3">'
            tmp += "<h1>ELIMINAR MODELO</h1> <br>"
            tmp += "Elimina las tablas del modelo de datos <br> "
            tmp += "------------------------------------------------------------------------------ <br>"
            tmp += 'Tablas eliminadas.'
            return tmp

if __name__ == "__main__":
    app.run(debug=True)