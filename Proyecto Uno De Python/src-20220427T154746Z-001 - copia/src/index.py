
import mysql.connector
from mysql.connector import Error
from django.shortcuts import render
from flask import Flask, render_template, request, redirect, url_for,flash

EmailSup= "SupervisorRadiator@hotmail.com"
ContraSup= "Supervisor"
EmailAcero= "EncargadoAcero@hotmail.com"
ContraAcero = "Acero"
EmailLimp = "EncargadoLimpieza@hotmail.com"
ContraLimp = "Limpieza"
EmailEns = "EncargadoEnsamblaje@hotmail.com"
ContraEns = "Ensamblaje"

app = Flask(__name__)
app.secret_key = 'RogueDragons'


@app.route('/')
def home():
    return render_template('inicio.html')



@app.route('/Login' , methods=['GET', 'POST'])
def Log():
        print(request.method)
        if request.method == 'POST':
                # pass # unknown
                print("Chekpoint :D")             
                Email = request.form.get('Correo')
                Contra = request.form.get('Contraseña')
                print("Chekpoint :D")
                print(Email,Contra)
                if Email == EmailSup and Contra == ContraSup:
                    return render_template("Graficar.html")
                elif Email == EmailEns and Contra == ContraEns:
                    return render_template("AreaEns.html")    
                elif Email == EmailAcero and Contra == ContraAcero:
                    return render_template("AreaAce.html")
                elif Email == EmailLimp and Contra == ContraLimp:
                    return render_template("AreaLimp.html")
                     

                
                elif request.method == 'GET':
            
                    Email = request.form.get('Email')
                    print("Chekpoint :D")
                    print(Email)
                    print()
                    print("No Post Back Call")
        return render_template("Error.html")


@app.route('/sobre')
def sobre():
    return render_template('Sobre.html')


@app.route('/AreaEnsablado')
def AreaEns():
    return render_template('AreaEns.html')



@app.route('/AreaLimpieza', methods=['GET', 'POST'])
def AreaLimp():
    return render_template('AreaLimp.html')



@app.route('/AreaAcero')
def AreaAce():
    return render_template('AreaAce.html')


@app.route('/UWU' , methods=['GET', 'POST'])
def Demo():
    return render_template('Prueba.html')




@app.route('/OWO' , methods=['GET', 'POST'])
def index():
        print(request.method)
        if request.method == 'POST':
                # pass # unknown
                print("Chekpoint :D")
                Edad = request.form.get('Edad')
                Age = 0
                Nombre = request.form.get('Nombre')
                Email = request.form.get('Email')
                
                print("Chekpoint :D")
                print(Email + Nombre + Edad)
                try:
                    connection = mysql.connector.connect(host='3.133.163.101',port='3306',database='maneskin',user='maneskin',password='1234')
                    if connection.is_connected():
                        db_Info = connection.get_server_info()
                        print("Connected to MySQL Server version XD", db_Info)
                        mycursor = connection.cursor()
                        sql = "INSERT INTO Demo (Nombre,Edad,Correo) VALUES (%s, %s, %s)"
                        val = (Nombre, int(Edad) ,Email)
                        mycursor.execute(sql,val)
                        connection.commit()  
                        print(mycursor.rowcount,"record") 
                        print("You're connected to database Listo")
                        mycursor.execute("SELECT * FROM Trabajador")
                        print(mycursor.fetchall())


                except Error as e:  
                    print("Error while connecting to MySQL", e)
                finally:
                    if connection.is_connected():
                        mycursor.close()
                        connection.close()
                        print("MySQL connection is closed")
                        return render_template("Success.html")
                    elif request.method == 'GET':
            
                        Email = request.form.get('Email')
                        print("Chekpoint :D")
                        print(Email)
                        print()
                        print("No Post Back Call")
        return render_template("Success.html")

@app.route('/DatosDeLim' , methods=['GET', 'POST'])
def LIMP():
        print(request.method)
        if request.method == 'POST':
                # pass # unknown
                print("Chekpoint :D")
                NuTra = request.form.get('Num Trabajadores')
                Nombre = request.form.get('Nombre')
                CostoP = request.form.get('Costo De P')
                PiezasLim = request.form.get('Piezas Lim')
                try:
                    connection = mysql.connector.connect(host='3.133.163.101',port='3306',database='maneskin',user='maneskin',password='1234')
                    if connection.is_connected():
                        db_Info = connection.get_server_info()
                        print("Connected to MySQL Server version XD", db_Info)
                        mycursor = connection.cursor()
                        sql = "INSERT INTO AreaLimpieza (Nombre,NumTrabajadores,CostoDeProduccion,PiezasLimpiadas) VALUES (%s, %s, %s, %s)"
                        val = (Nombre, int(NuTra) ,float(CostoP),int(PiezasLim))
                        mycursor.execute(sql,val)
                        connection.commit()  
                        print(mycursor.rowcount,"record") 
                        print("You're connected to database Listo")
                        mycursor.execute("SELECT * FROM AreaLimpieza")
                        print(mycursor.fetchall())


                except Error as e:  
                    print("Error while connecting to MySQL", e)
                finally:
                    if connection.is_connected():
                        mycursor.close()
                        connection.close()
                        print("MySQL connection is closed")
                        return render_template("Success.html")
                    elif request.method == 'GET':
            
                        Email = request.form.get('Email')
                        print("Chekpoint :D")
                        print(Email)
                        print()
                        print("No Post Back Call")
                
                print("Chekpoint :D")
                print(NuTra + Nombre + CostoP + PiezasLim)
                return render_template("Success.html")
        elif request.method == 'GET':
            
            Email = request.form.get('Email')
            print("Chekpoint :D")
            print(Email)
            print()
            print("No Post Back Call")
        return render_template("Success.html")



@app.route('/DatosDeEns',methods=['GET', 'POST'] )
def Ens():
        print(request.method)
        if request.method == 'POST':
                # pass # unknown
                print("Chekpoint :D")
                NuTra = request.form.get('Num Trabajadores')
                Age = 0
                Nombre = request.form.get('Nombre')
                CostoP = request.form.get('Costo De P')
                CantEsta = request.form.get('Cant Estaño')
                LitFlu = request.form.get('Litros De Flux')
                TimEns = request.form.get('Tiempo Ens')
                
                print("Chekpoint :D")
                print(NuTra + Nombre + CostoP)
                try:
                    connection = mysql.connector.connect(host='3.133.163.101',port='3306',database='maneskin',user='maneskin',password='1234')
                    if connection.is_connected():
                        db_Info = connection.get_server_info()
                        print("Connected to MySQL Server version XD", db_Info)
                        mycursor = connection.cursor()
                        sql = "INSERT INTO AreaEnsamblado (Nombre,NumTrabajadores,CostoDeProduccion,CantEstano,LitrosFlux,TiempoEns) VALUES (%s, %s, %s, %s, %s, %s)"
                        val = (Nombre, int(NuTra) ,float(CostoP),float(CantEsta),float(LitFlu),float(TimEns))
                        mycursor.execute(sql,val)
                        connection.commit()  
                        print(mycursor.rowcount,"record") 
                        print("You're connected to database Listo")
                        mycursor.execute("SELECT * FROM Trabajador")
                        print(mycursor.fetchall())


                except Error as e:  
                    print("Error while connecting to MySQL", e)
                finally:
                    if connection.is_connected():
                        mycursor.close()
                        connection.close()
                        print("MySQL connection is closed")
                        return render_template("Success.html")
                    elif request.method == 'GET':
            
                        Email = request.form.get('Email')
                        print("Chekpoint :D")
                        print(Email)
                        print()
                        print("No Post Back Call")
        return render_template("Success.html")

@app.route('/PruebaCON',methods=['GET', 'POST'] )
def PruebaCON():
    return render_template('pruebaCON.html')              


@app.route('/DatosDeAce',methods=['GET', 'POST'] )
def Ace():
        print(request.method)
        if request.method == 'POST':
                # pass # unknown
                print("Chekpoint :D")
                NuTra = request.form.get('Num Trabajadores')
                Age = 0
                Nombre = request.form.get('Nombre')
                CostoP = request.form.get('Costo De P')
                CantPzaE = request.form.get('Cant De Pza Ende')
                CantPer = request.form.get('Cant De Perdida')
                
                
                print("Chekpoint :D")
                print(NuTra + Nombre + CostoP)
                try:
                    connection = mysql.connector.connect(host='3.133.163.101',port='3306',database='maneskin',user='maneskin',password='1234')
                    if connection.is_connected():
                        db_Info = connection.get_server_info()
                        print("Connected to MySQL Server version XD", db_Info)
                        mycursor = connection.cursor()
                        sql = "INSERT INTO AreaAcero (Nombre,NumTrabajadores,CostoDeProduccion,CantidadDePzaEnderezadas,CantidadPerdida) VALUES (%s, %s, %s, %s, %s)"
                        val = (Nombre, int(NuTra) ,float(CostoP),int(CantPzaE),int(CantPer))
                        mycursor.execute(sql,val)
                        connection.commit()  
                        print(mycursor.rowcount,"record") 
                        print("You're connected to database Listo")
                        mycursor.execute("SELECT * FROM Trabajador")
                        print(mycursor.fetchall())


                except Error as e:  
                    print("Error while connecting to MySQL", e)
                finally:
                    if connection.is_connected():
                        mycursor.close()
                        connection.close()
                        print("MySQL connection is closed")
                        return render_template("Success.html")
                    elif request.method == 'GET':
            
                        Email = request.form.get('Email')
                        print("Chekpoint :D")
                        print(Email)
                        print()
                        print("No Post Back Call")
        return render_template("Success.html")


@app.route('/Graficacion')
def Graficacion():
    return render_template('Graficar.html')



if __name__ == '__main__':
    app.run(debug = True)   