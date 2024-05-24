from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import pymysql
import os
import webbrowser
#from fpdf import FPDF
#from weasyprint import HTML

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

###Idiomas


@app.route('/idioma')
def idioma():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma order by idIdioma')
    datos = cursor.fetchall()
    return render_template("idioma.html", comentarios = datos)

@app.route('/idioma_agregar')
def idioma_agregar():
    return render_template("idioma_agr.html")


@app.route('/idioma_fagrega', methods=['POST'])
def idioma_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into idioma (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('idioma'))

@app.route('/idioma_editar/<string:id>')
def idioma_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma where idIdioma = %s', (id))
    dato  = cursor.fetchall()
    return render_template("idioma_edi.html", comentar=dato[0])

@app.route('/idioma_fedita/<string:id>',methods=['POST'])
def idioma_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('update idioma set descripcion=%s where idIdioma=%s', (desc,id))
        conn.commit()
    return redirect(url_for('idioma'))

@app.route('/idioma_borrar/<string:id>')
def idioma_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from idioma where idIdioma = {0}'.format(id))
    conn.commit()
    return redirect(url_for('idioma'))

###habilidades

@app.route('/habilidad')
def habilidad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, descripcion from habilidad order by idHabilidad')
    datos = cursor.fetchall()
    return render_template("habilidad.html", comentarios = datos)

@app.route('/habilidad_agregar')
def habilidad_agregar():
    return render_template("habilidad_agr.html")


@app.route('/habilidad_fagrega', methods=['POST'])
def habilidad_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into habilidad (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('habilidad'))

@app.route('/habilidad_editar/<string:id>')
def habilidad_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, descripcion from habilidad where idHabilidad = %s', (id))
    dato  = cursor.fetchall()
    return render_template("habilidad_edi.html", comentar=dato[0])

@app.route('/habilidad_fedita/<string:id>',methods=['POST'])
def habilidad_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('update habilidad set descripcion=%s where idHabilidad=%s', (desc,id))
        conn.commit()
    return redirect(url_for('habilidad'))

@app.route('/habilidad_borrar/<string:id>')
def habilidad_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from habilidad where idHabilidad = {0}'.format(id))
    conn.commit()
    return redirect(url_for('habilidad'))


@app.route('/gradoAvance')
def gradoAvance():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idGradoAvance, descripcion from grado_avance order by idGradoAvance')
    datos = cursor.fetchall()
    return render_template("gradoAvance.html", comentarios = datos)

@app.route('/grado_agregar')
def grado_agregar():
    return render_template("grado_agr.html")


@app.route('/grado_fagrega', methods=['POST'])
def grado_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into grado_avance (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('gradoAvance'))

@app.route('/grado_editar/<string:id>')
def grado_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idGradoAvance, descripcion from grado_avance where idGradoAvance = %s', (id))
    dato  = cursor.fetchall()
    return render_template("grado_edi.html", comentar=dato[0])

@app.route('/grado_fedita/<string:id>',methods=['POST'])
def grado_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('update grado_avance set descripcion=%s where idGradoAvance=%s', (desc,id))
        conn.commit()
    return redirect(url_for('gradoAvance'))

@app.route('/grado_borrar/<string:id>')
def grado_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from grado_avance where idGradoAvance = {0}'.format(id))
    conn.commit()
    return redirect(url_for('gradoAvance'))

@app.route('/area')
def area():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area order by idArea')
    datos = cursor.fetchall()
    return render_template("area.html", comentarios = datos)

@app.route('/area_editar/<string:id>')
def area_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area where idArea = %s', (id))
    dato  = cursor.fetchall()
    return render_template("area_edi.html", comentar=dato[0])

@app.route('/area_fedita/<string:id>',methods=['POST'])
def area_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('update area set descripcion=%s where idArea=%s', (desc,id))
        conn.commit()
    return redirect(url_for('area'))

@app.route('/area_borrar/<string:id>')
def area_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from area where idArea = {0}'.format(id))
    conn.commit()
    return redirect(url_for('area'))

@app.route('/area_agregar')
def area_agregar():
    return render_template("area_agr.html")

@app.route('/area_fagrega', methods=['POST'])
def area_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into area (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('area'))



@app.route('/puesto')
def puesto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    return render_template("puesto.html", pue = datos, dat='   ', catArea = '   ', catEdoCivil = '   ', catEscolaridad = '   ',
                           catGradoAvance = '    ', catCarrera = '    ', catIdioma = ' ', catHabilidad = ' ')


@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
            'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
            'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s', (idP))
    datos2 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idP))
    datos3 = cursor.fetchall()

    cursor.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s', (idP))
    datos4 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos5 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos6 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos7 = cursor.fetchall()
    return render_template("puesto.html", pue = datos, dat=dato[0], catArea=datos1[0], catEdoCivil=datos2[0], catEscolaridad=datos3[0],
                           catGradoAvance=datos4[0], catCarrera=datos5[0], catIdioma=datos6, catHabilidad=datos7)

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from puesto where idPuesto = %s',(idP))
    conn.commit()
    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()
    return redirect(url_for('puesto'))


@app.route('/puesto_agrOp2')
def puesto_agrOp2():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, descripcion from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = cursor.fetchall()

    return render_template("puesto_agrOp2.html", catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7)


@app.route('/puesto_fagrega2', methods=['POST'])
def puesto_fagrega():
    if request.method == 'POST':

        if  'idArea' in request.form:
            idAr = request.form['idArea']
        else:
            idAr = '1'
        if 'idEstadoCivil' in request.form:
            idEC = request.form['idEstadoCivil']
        else:
            idEC = '1'
        if 'idEscolaridad' in request.form:
            idEs = request.form['idEscolaridad']
        else:
            idEs = '1'
        if 'idGradoAvance' in request.form:
            idGA = request.form['idGradoAvance']
        else:
            idGA = '1'
        if 'idCarrera' in request.form:
            idCa = request.form['idCarrera']
        else:
            idCa = '1'
        if 'sexo' in request.form:
            sex = request.form['sexo']
        else:
            sex = '1'
        codP = request.form['codPuesto']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']


    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute(
    'insert into puesto (codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
    'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
    'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
    (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda, sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF,
     reqP, resp, conT))
    conn.commit()

    cursor.execute('select idPuesto from puesto where idPuesto=(select max(idPuesto) from puesto) ')
    dato = cursor.fetchall()
    idpue = dato[0]
    idP = idpue[0]

    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP, i))
            conn.commit()

    cursor.execute('select count(*) from habilidad ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh =nhab[0]+1

    for i in range(1,nh):
        habi = 'h' + str(i)
        if habi in request.form:
            cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)', (idP,i))
            conn.commit()

    return redirect(url_for('puesto'))



@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
        'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
        'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, descripcion from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos11 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s',(idP))
    datos12 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s',(idP))
    datos13 = cursor.fetchall()

    cursor.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s',(idP))
    datos14 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos15 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos16 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos17 = cursor.fetchall()


    return render_template("puesto_edi.html", dat=dato[0], catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7,
                           Area=datos11[0], EdoCivil=datos12[0], Escolaridad=datos13[0], GradoAvance=datos14[0],
                           Carrera=datos15[0], Idioma=datos16, Habilidad=datos17)


@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
    if request.method == 'POST':
        codP = request.form['codPuesto']
        idAr = request.form['idArea']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        sex = request.form['sexo']
        idEC = request.form['idEstadoCivil']
        idEs = request.form['idEscolaridad']
        idGA = request.form['idGradoAvance']
        idCa = request.form['idCarrera']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()

    cursor.execute('update puesto set codPuesto = %s, idArea = %s, nomPuesto = %s, puestoJefeSup = %s, jornada = %s, '
                   'remunMensual = %s, prestaciones = %s, descripcionGeneral = %s, funciones = %s, edad = %s, sexo = %s, '
                   'idEstadoCivil = %s, idEscolaridad = %s, idGradoAvance = %s, idCarrera = %s, experiencia = %s, '
                   'conocimientos = %s, manejoEquipo = %s, reqFisicos = %s, reqPsicologicos = %s, responsabilidades = %s, '
                   'condicionesTrabajo = %s where idPuesto = %s', (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda,
                   sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT, idP))
    conn.commit()

    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()

    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP, i))
            conn.commit()

    cursor.execute('select count(*) from habilidad ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh = nhab[0] + 1

    for i in range(1, nh):
        habi = 'h' + str(i)
        if habi in request.form:
            cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)', (idP, i))
            conn.commit()
    return redirect(url_for('puesto'))



@app.route('/carrera')
def carrera():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idCarrera, descripcion FROM carrera ORDER BY idCarrera")
    dato = cursor.fetchall()
    return render_template("carrera.html", datos = dato)

@app.route('/carre_agregar')
def agreCarre():
    return render_template("carre_agre.html")

@app.route("/agregarCarre", methods=['POST'])
def agregarCarrera():
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO carrera (descripcion) VALUES (%s)", (descrip))
        conn.commit()
    return redirect(url_for('carrera'))

@app.route("/carre_editar/<string:idd>")
def editarcarre(idd):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idCarrera, descripcion FROM carrera WHERE idCarrera=%s", (idd))
    dato = cursor.fetchall()
    return render_template("editarCarre.html", dato = dato[0])

@app.route("/updateCarre/<string:idd>", methods=['POST'])
def updateCarre(idd):
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("UPDATE carrera SET descripcion = %s WHERE idCarrera = %s", (descrip, idd))
        conn.commit()
    return redirect(url_for('carrera'))

@app.route("/carre_borrar/<string:idd>")
def borrarCarre(idd):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM carrera WHERE idCarrera = %s", (idd))
    conn.commit()
    return redirect(url_for('carrera'))



@app.route("/escolaridad")
def escolaridad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idEscolaridad, descripcion FROM escolaridad ORDER BY idEscolaridad")
    datos = cursor.fetchall()
    return render_template("escolaridad.html", datos = datos)

@app.route("/esco_agregar")
def agreEsco():
    return render_template("esco_agre.html")

@app.route("/agregarEsco", methods=['POST'])
def agregarEscolaridad():
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO escolaridad (descripcion) VALUES (%s)", (descrip))
        conn.commit()
    return redirect(url_for("escolaridad"))

@app.route("/esco_editar/<string:idd>")
def editarEsco(idd):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idEscolaridad, descripcion FROM escolaridad WHERE idEscolaridad = %s", (idd))
    dato = cursor.fetchall()
    return render_template("editarEsco.html", dato = dato[0])

@app.route("/updateEsco/<string:idd>", methods=['POST'])
def updateEsco(idd):
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("UPDATE escolaridad SET descripcion = %s WHERE idEscolaridad = %s", (descrip, idd))
        conn.commit()
    return redirect(url_for('escolaridad'))

@app.route("/esco_borrar/<string:idd>")
def borrarEsco(idd):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM escolaridad WHERE idEscolaridad = %s", (idd))
    conn.commit()
    return redirect(url_for("escolaridad"))


@app.route("/edocivil")
def edocivil():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idEstadoCivil, descripcion FROM estado_civil ORDER BY idEstadoCivil")
    datos = cursor.fetchall()
    return render_template("edoCivil.html", datos = datos)

@app.route("/edociv_agregar")
def agreEdoCiv():
    return render_template("edociv_agre.html")

@app.route("/agregarEdociv", methods=['POST'])
def agregarEdoCiv():
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO estado_civil (descripcion) VALUES (%s)", (descrip))
        conn.commit()
    return redirect(url_for("edocivil"))

@app.route("/edoc_editar/<string:idd>")
def editarEdociv(idd):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idEstadoCivil, descripcion FROM estado_civil WHERE idEstadoCivil = %s", (idd))
    dato = cursor.fetchall()
    return render_template("editarEdociv.html", dato = dato[0])

@app.route("/updateEdociv/<string:idd>", methods=['POST'])
def updateEdociv(idd):
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("UPDATE estado_civil SET descripcion = %s WHERE idEstadoCivil = %s", (descrip, idd))
        conn.commit()
    return redirect(url_for("edocivil"))

@app.route("/edoc_borrar/<string:idd>")
def borrarEdociv(idd):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM estado_civil WHERE idEstadoCivil = %s", (idd))
    conn.commit()
    return redirect(url_for("edocivil"))



@app.route("/candidatos")
def candidatos():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT b.folio, a.idVacante, c.nomPuesto, a.candidatoSelecc FROM vacante a, requisicion b, puesto c WHERE a.idRequisicion=b.idRequisicion AND a.idPuesto=c.idPuesto AND b.idPuesto=c.idPuesto")
    datos = cursor.fetchall()
    return render_template("candidatos.html", datos = datos)


@app.route("/capturarCand/<string:idV>")
def capturarCandidatos(idV):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT b.folio, a.idVacante, c.nomPuesto FROM vacante a, requisicion b, puesto c WHERE a.idRequisicion=b.idRequisicion AND a.idPuesto=c.idPuesto AND b.idPuesto=c.idPuesto AND a.idVacante=%s", (idV))
    datos = cursor.fetchall()
    
    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    return render_template("capturarCand.html", dato = datos[0], catEdoCivil=datos2, catEscolaridad=datos3, catGradoAvance=datos4, catCarrera=datos5)


@app.route("/seleccionCand/<string:idV>")
def verCandidatosVacante(idV):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT b.nomPuesto FROM puesto b, vacante a WHERE a.idVacante=%s AND a.idPuesto=b.idPuesto", (idV))
    nomPuestoVacante = cursor.fetchall()
    cursor.execute("SELECT a.idCandidato, a.idVacante, a.idRequisicion, a.nombre, a.CURP FROM candidato a, vacante b WHERE a.idVacante=%s AND a.idVacante=b.idVacante", (idV))
    datos = cursor.fetchall()
    cursor.execute("SELECT candidatoSelecc FROM vacante WHERE idVacante = %s", (idV))
    idCandSelecc = cursor.fetchall()
    return render_template("candVacan.html", datos = datos, nomPuesto = nomPuestoVacante[0][0], idV = idV, idCandSelec = idCandSelecc[0][0])


@app.route("/candSelec/<string:idC>/<string:idV>")
def showSelectedCand(idC, idV):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor() 
    cursor.execute("SELECT a.idCandidato, a.idVacante, a.idRequisicion, a.idPuesto, b.folio, c.nomPuesto, a.CURP, a.RFC, a.nombre, a.domCalle, a.domNumExtInt, a.domColonia, a.tel1, a.tel2, a.correoE, a.edad, a.sexo, a.idEstadoCivil, a.idEscolaridad, a.idGradoAvance, a.idCarrera, "
                   "a.entrevSelecReq, a.entrevSelecPresen, a.entrevSelecResult, a.evalMedicaReq, a.evalMedicaPresen, a.evalMedicaResult, a.evalPsicolgReq, a.evalPsicologPresen, a.evalPsicologResult, a.evalPsicometReq, a.evalPsicometPresene, a.evalPsicometResult, "
                   "a.evalTecnicaReq, a.evalTecnicaPresen, a.evalTecnicaResult, a.evalConocReq, a.evalConocPresen, a.evalConocResult, a.entrevFinalReq, a.entrevFinalPresen, a.entrevFinalResul FROM candidato a, requisicion b, puesto c "
                   "WHERE a.idCandidato=%s AND a.idRequisicion=b.idRequisicion AND a.idPuesto=c.idPuesto", (idC))
    datos = cursor.fetchall()

    cursor.execute("SELECT b.descripcion FROM candidato a, estado_civil b WHERE a.idCandidato=%s AND a.idEstadoCivil=b.idEstadoCivil", (idC))
    edocCandSelec = cursor.fetchall()

    cursor.execute("SELECT b.descripcion FROM candidato a, escolaridad b WHERE a.idCandidato=%s AND a.idEscolaridad=b.idEscolaridad", (idC))
    escoCandSelec = cursor.fetchall()

    cursor.execute("SELECT b.descripcion FROM candidato a, grado_avance b WHERE a.idCandidato=%s AND a.idGradoAvance=b.idGradoAvance", (idC))
    gdoavanCandSelec = cursor.fetchall()

    cursor.execute("SELECT b.descripcion FROM candidato a, carrera b WHERE a.idCandidato=%s AND a.idCarrera=b.idCarrera", (idC))
    carreCandSelec = cursor.fetchall()

    return render_template("candSelecc.html", datos = datos[0], edocCandSelec = edocCandSelec[0][0], escoCandSelec = escoCandSelec[0][0], gdoavanCandSelec = gdoavanCandSelec[0][0], carreCandSelec = carreCandSelec[0][0], idV=idV)





@app.route("/borrarCand/<string:idC>/<string:idV>")
def borrarCand(idC, idV):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor() 
    cursor.execute("SELECT candidatoSelecc FROM vacante WHERE idVacante=%s", (idV))
    idCandSelec = cursor.fetchall()

    if int(idCandSelec[0][0]) == int(idC):
        cursor.execute("UPDATE vacante SET candidatoSelecc=0 WHERE idVacante=%s", (idV))
        conn.commit()

    cursor.execute("DELETE FROM candidato WHERE idCandidato=%s", (idC))
    conn.commit()
    return redirect(url_for("verCandidatosVacante", idV = idV))

@app.route("/seleccionarCandidato/<string:idC>/<string:idV>")
def seleccionarCandidato(idC, idV):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("UPDATE vacante SET candidatoSelecc = %s WHERE idVacante = %s", (idC, idV))
    conn.commit()
    return redirect(url_for("verCandidatosVacante", idV = idV))


@app.route("/captCand", methods=['GET', 'POST'])
def capturarCandidato():
    if request.method == 'POST':
        idVacan = request.form.get('idVacante', '')
        curp = request.form.get('curp', '').strip()
        rfc = request.form.get('rfc', '').strip()
        nombre = request.form.get('nombre', '').strip()
        calle = request.form.get('Calle', '').strip()
        num = request.form.get('numExtInt', '')
        colonia = request.form.get('domColonia', '').strip()
        tel1 = request.form.get('tel1', '')
        tel2 = request.form.get('tel2', '')
        correo = request.form.get('correo', '').strip()
        edad = request.form.get('Edad', '')
        sex = request.form.get('sexo', '')
        edoc = request.form.get('idEstadoCivil', '')
        esco = request.form.get('idEscolaridad', '')
        gdoavan = request.form.get('idGradoAvance', '1')
        carre = request.form.get('idCarrera', '1')

        entrereq = request.form.get('entrevistaReq', '')
        entrepres = request.form.get('entrevistaPres', '')
        entreresul = request.form.get('campoEntrevista', 'NO APLICA/NO PRESENTADA').strip()
        evalMedicReq = request.form.get('evalMedicaReq', '')
        evalMedicPres = request.form.get('evalMedicaPres', '')
        evalMedicResul = request.form.get('campoEvalMedica', 'NO APLICA/NO PRESENTADA').strip()
        evalPsicolReq = request.form.get('evalPsicoloReq', '')
        evalPsicolPres = request.form.get('evalPsicoloPres', '')
        evalPsicolResul = request.form.get('campoEvalPsicolo', 'NO APLICA/NO PRESENTADA').strip()
        evalPsicomReq = request.form.get('evalPsicomReq', '')
        evalPsicomPres = request.form.get('evalPsicomPres', '')
        evalPsicomResul = request.form.get('campoEvalPsicom', 'NO APLICA/NO PRESENTADA').strip()
        evalTecReq = request.form.get('evalTecniReq', '')
        evalTecPres = request.form.get('evalTecniPres', '')
        evalTecResul = request.form.get('campoEvalTecni', 'NO APLICA/NO PRESENTADA').strip()
        evalConocReq = request.form.get('evalConoReq', '')
        evalConocPres = request.form.get('evalConoPres', '')
        evalConocResul = request.form.get('campoEvalCono', 'NO APLICA/NO PRESENTADA').strip()
        entreFinReq = request.form.get('entrevistaFinReq', '')
        entreFinPres = request.form.get('entrevistaFinPres', '')
        entreFinResul = request.form.get('campoEntrevistaFin', 'NO APLICA/NO PRESENTADA').strip()

        print("idVacante:", idVacan)
        print("curp:", curp)
        print("rfc:", rfc)
        print("nombre:", nombre)
        print("calle:", calle)
        print("numExtInt:", num)
        print("domColonia:", colonia)
        print("tel1:", tel1)
        print("tel2:", tel2)
        print("correo:", correo)
        print("Edad:", edad)
        print("sexo:", sex)
        print("idEstadoCivil:", edoc)
        print("idEscolaridad:", esco)
        print("idGradoAvance:", gdoavan)
        print("idCarrera:", carre)
        print("entrevistaReq:", entrereq)
        print("entrevistaPres:", entrepres)
        print("campoEntrevista:", entreresul)
        print("evalMedicaReq:", evalMedicReq)
        print("evalMedicaPres:", evalMedicPres)
        print("campoEvalMedica:", evalMedicResul)
        print("evalPsicoloReq:", evalPsicolReq)
        print("evalPsicoloPres:", evalPsicolPres)
        print("campoEvalPsicolo:", evalPsicolResul)
        print("evalPsicomReq:", evalPsicomReq)
        print("evalPsicomPres:", evalPsicomPres)
        print("campoEvalPsicom:", evalPsicomResul)
        print("evalTecniReq:", evalTecReq)
        print("evalTecniPres:", evalTecPres)
        print("campoEvalTecni:", evalTecResul)
        print("evalConoReq:", evalConocReq)
        print("evalConoPres:", evalConocPres)
        print("campoEvalCono:", evalConocResul)
        print("entrevistaFinReq:", entreFinReq)
        print("entrevistaFinPres:", entreFinPres)
        print("campoEntrevistaFin:", entreFinResul)

        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("SELECT idRequisicion, idPuesto FROM vacante WHERE idVacante = %s", (idVacan))
        ids = cursor.fetchall()

        cursor.execute("INSERT INTO candidato (idVacante, idRequisicion, idPuesto, CURP, RFC, nombre, domCalle, domNumExtInt, domColonia, tel1, tel2, correoE, edad, sexo, "
                        "idEstadoCivil, idEscolaridad, idGradoAvance, idCarrera, entrevSelecReq, entrevSelecPresen, entrevSelecResult, evalMedicaReq, evalMedicaPresen, "
                        "evalMedicaResult, evalPsicolgReq, evalPsicologPresen, evalPsicologResult, evalPsicometReq, evalPsicometPresene, evalPsicometResult, "
                        "evalTecnicaReq, evalTecnicaPresen, evalTecnicaResult, evalConocReq, evalConocPresen, evalConocResult, entrevFinalReq, entrevFinalPresen, entrevFinalResul) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                        (idVacan, ids[0][0], ids[0][1], curp, rfc, nombre, calle, num, colonia, tel1, tel2, correo, edad, sex, edoc, esco, gdoavan, carre, entrereq, entrepres, entreresul, 
                        evalMedicReq, evalMedicPres, evalMedicResul, evalPsicolReq, evalPsicolPres, evalPsicolResul, evalPsicomReq, evalPsicomPres, evalPsicomResul, evalTecReq, evalTecPres,
                        evalTecResul, evalConocReq, evalConocPres, evalConocResul, entreFinReq, entreFinPres, entreFinResul))
        conn.commit()

    return redirect(url_for("candidatos"))


@app.route("/detailCand/<string:idC>")
def detallesCandidato(idC):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT a.idCandidato, a.idVacante, a.idRequisicion, a.idPuesto, b.folio, c.nomPuesto, a.CURP, a.RFC, a.nombre, a.domCalle, a.domNumExtInt, a.domColonia, a.tel1, a.tel2, a.correoE, a.edad, a.sexo, a.idEstadoCivil, a.idEscolaridad, a.idGradoAvance, a.idCarrera, "
                   "a.entrevSelecReq, a.entrevSelecPresen, a.entrevSelecResult, a.evalMedicaReq, a.evalMedicaPresen, a.evalMedicaResult, a.evalPsicolgReq, a.evalPsicologPresen, a.evalPsicologResult, a.evalPsicometReq, a.evalPsicometPresene, a.evalPsicometResult, "
                   "a.evalTecnicaReq, a.evalTecnicaPresen, a.evalTecnicaResult, a.evalConocReq, a.evalConocPresen, a.evalConocResult, a.entrevFinalReq, a.entrevFinalPresen, a.entrevFinalResul FROM candidato a, requisicion b, puesto c "
                   "WHERE a.idCandidato=%s AND a.idRequisicion=b.idRequisicion AND a.idPuesto=c.idPuesto", (idC))
    datosCand = cursor.fetchall()

    cursor.execute("SELECT b.descripcion FROM candidato a, estado_civil b WHERE a.idCandidato=%s AND a.idEstadoCivil=b.idEstadoCivil", (idC))
    edocCand = cursor.fetchall()

    cursor.execute("SELECT b.descripcion FROM candidato a, escolaridad b WHERE a.idCandidato=%s AND a.idEscolaridad=b.idEscolaridad", (idC))
    escoCand = cursor.fetchall()

    cursor.execute("SELECT b.descripcion FROM candidato a, grado_avance b WHERE a.idCandidato=%s AND a.idGradoAvance=b.idGradoAvance", (idC))
    gdoavanCand = cursor.fetchall()

    cursor.execute("SELECT b.descripcion FROM candidato a, carrera b WHERE a.idCandidato=%s AND a.idCarrera=b.idCarrera", (idC))
    carreCand = cursor.fetchall()

    return render_template("detallesCand.html", datosCand = datosCand[0], edocCand = edocCand[0][0], escoCand = escoCand[0][0], gdoavanCand = gdoavanCand[0][0], carreCand = carreCand[0][0])


@app.route("/unselectCand/<string:idV>")
def deseleccionarCandidato(idV):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("UPDATE vacante SET candidatoSelecc=0 WHERE idVacante=%s", (idV))
    conn.commit()
    return redirect(url_for("candidatos"))

@app.route("/editarCand/<string:idC>/<string:idV>")
def editarCand(idC, idV):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT b.folio, a.idVacante, c.nomPuesto FROM vacante a, requisicion b, puesto c WHERE a.idRequisicion=b.idRequisicion AND a.idPuesto=c.idPuesto AND b.idPuesto=c.idPuesto AND a.idVacante=%s", (idV))
    datos = cursor.fetchall()
    
    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute("SELECT idVacante, idRequisicion, idPuesto, CURP, RFC, nombre, domCalle, domNumExtInt, domColonia, tel1, tel2, correoE, edad, sexo, "
                        "idEstadoCivil, idEscolaridad, idGradoAvance, idCarrera, entrevSelecReq, entrevSelecPresen, entrevSelecResult, evalMedicaReq, evalMedicaPresen, "
                        "evalMedicaResult, evalPsicolgReq, evalPsicologPresen, evalPsicologResult, evalPsicometReq, evalPsicometPresene, evalPsicometResult, "
                        "evalTecnicaReq, evalTecnicaPresen, evalTecnicaResult, evalConocReq, evalConocPresen, evalConocResult, entrevFinalReq, entrevFinalPresen, entrevFinalResul, idCandidato FROM candidato WHERE idCandidato = %s", (idC)
                        )
    datosOp = cursor.fetchall()
    return render_template("editarCand.html", dato = datos[0], catEdoCivil=datos2, catEscolaridad=datos3, catGradoAvance=datos4, catCarrera=datos5, datosOp=datosOp[0] )

@app.route("/editarCandFunct/<string:idC>", methods=['GET', 'POST'])
def editarCandFunct(idC):
    if request.method == "POST":
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        idVacan = request.form.get('idVacante')
        curp = request.form.get('curp')
        rfc = request.form.get('rfc')
        nombre = request.form.get('nombre')
        calle = request.form.get('Calle')
        num = request.form.get('numExtInt')
        colonia = request.form.get('domColonia')
        tel1 = request.form.get('tel1')
        tel2 = request.form.get('tel2')
        correo = request.form.get('correo')
        edad = request.form.get('Edad')
        sex = request.form.get('sexo')
        edoc = request.form.get('idEstadoCivil')
        esco = request.form.get('idEscolaridad')
        gdoavan = request.form.get('idGradoAvance', '1')
        carre = request.form.get('idCarrera', '1')


        entrereq = request.form.get('entrevistaReq', '')
        entrepres = request.form.get('entrevistaPres', '')
        entreresul = request.form.get('campoEntrevista', 'NO APLICA/NO PRESENTADA').strip()
        evalMedicReq = request.form.get('evalMedicaReq', '')
        evalMedicPres = request.form.get('evalMedicaPres', '')
        evalMedicResul = request.form.get('campoEvalMedica', 'NO APLICA/NO PRESENTADA').strip()
        evalPsicolReq = request.form.get('evalPsicoloReq', '')
        evalPsicolPres = request.form.get('evalPsicoloPres', '')
        evalPsicolResul = request.form.get('campoEvalPsicolo', 'NO APLICA/NO PRESENTADA').strip()
        evalPsicomReq = request.form.get('evalPsicomReq', '')
        evalPsicomPres = request.form.get('evalPsicomPres', '')
        evalPsicomResul = request.form.get('campoEvalPsicom', 'NO APLICA/NO PRESENTADA').strip()
        evalTecReq = request.form.get('evalTecniReq', '')
        evalTecPres = request.form.get('evalTecniPres', '')
        evalTecResul = request.form.get('campoEvalTecni', 'NO APLICA/NO PRESENTADA').strip()
        evalConocReq = request.form.get('evalConoReq', '')
        evalConocPres = request.form.get('evalConoPres', '')
        evalConocResul = request.form.get('campoEvalCono', 'NO APLICA/NO PRESENTADA').strip()
        entreFinReq = request.form.get('entrevistaFinReq', '')
        entreFinPres = request.form.get('entrevistaFinPres', '')
        entreFinResul = request.form.get('campoEntrevistaFin', 'NO APLICA/NO PRESENTADA').strip()

        print("idVacante:", idVacan)
        print("curp:", curp)
        print("rfc:", rfc)
        print("nombre:", nombre)
        print("calle:", calle)
        print("numExtInt:", num)
        print("domColonia:", colonia)
        print("tel1:", tel1)
        print("tel2:", tel2)
        print("correo:", correo)
        print("Edad:", edad)
        print("sexo:", sex)
        print("idEstadoCivil:", edoc)
        print("idEscolaridad:", esco)
        print("idGradoAvance:", gdoavan)
        print("idCarrera:", carre)
        print("entrevistaReq:", entrereq)
        print("entrevistaPres:", entrepres)
        print("campoEntrevista:", entreresul)
        print("evalMedicaReq:", evalMedicReq)
        print("evalMedicaPres:", evalMedicPres)
        print("campoEvalMedica:", evalMedicResul)
        print("evalPsicoloReq:", evalPsicolReq)
        print("evalPsicoloPres:", evalPsicolPres)
        print("campoEvalPsicolo:", evalPsicolResul)
        print("evalPsicomReq:", evalPsicomReq)
        print("evalPsicomPres:", evalPsicomPres)
        print("campoEvalPsicom:", evalPsicomResul)
        print("evalTecniReq:", evalTecReq)
        print("evalTecniPres:", evalTecPres)
        print("campoEvalTecni:", evalTecResul)
        print("evalConoReq:", evalConocReq)
        print("evalConoPres:", evalConocPres)
        print("campoEvalCono:", evalConocResul)
        print("entrevistaFinReq:", entreFinReq)
        print("entrevistaFinPres:", entreFinPres)
        print("campoEntrevistaFin:", entreFinResul)
        print("idCandidato", idC)

        cursor.execute("UPDATE candidato SET idVacante = %s, CURP = %s, RFC = %s, nombre = %s, domCalle = %s, domNumExtInt = %s, domColonia = %s, tel1 = %s, tel2 = %s, correoE = %s, edad = %s, sexo = %s, idEstadoCivil = %s, idEscolaridad = %s, idGradoAvance = %s, idCarrera = %s, entrevSelecReq = %s, entrevSelecPresen = %s, entrevSelecResult = %s, evalMedicaReq = %s, evalMedicaPresen = %s, evalMedicaResult = %s, evalPsicolgReq = %s, evalPsicologPresen = %s, evalPsicologResult = %s, evalPsicometReq = %s, evalPsicometPresene = %s, evalPsicometResult = %s, evalTecnicaReq = %s, evalTecnicaPresen = %s, evalTecnicaResult = %s, evalConocReq = %s, evalConocPresen = %s, evalConocResult = %s, entrevFinalReq = %s, entrevFinalPresen = %s, entrevFinalResul = %s WHERE idCandidato = %s",
                                            (idVacan, curp, rfc, nombre, calle, num, colonia, tel1, tel2, correo, edad, sex, edoc, esco, gdoavan, carre, entrereq, entrepres, entreresul, evalMedicReq, evalMedicPres, evalMedicResul,  evalPsicolReq,evalPsicolPres,evalPsicolResul,evalPsicomReq,evalPsicomPres,evalPsicomResul,evalTecReq,evalTecPres,evalTecResul,evalConocReq,evalConocPres,evalConocResul,entreFinReq,entreFinPres, entreFinResul, idC))
        conn.commit()
        return redirect(url_for('candidatos'))
    


@app.route('/requisicion')
def requisicion():
    return render_template("requisicion.html")




def obtener_requisicion(requisicion_id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM requisicion WHERE idRequisicion = %s", (requisicion_id,))
    requisicion = cursor.fetchone()
    cursor.close()
    conn.close()
    return requisicion

@app.route('/mostrar_requisicion')
def mostrar_requisicion():
    requisicion_id = request.args.get('id')
    requisicion = obtener_requisicion(requisicion_id)
    return render_template("requisicion_revisa.html", requisicion=requisicion)

@app.route('/listar_requisiciones')
def listar_requisiciones():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM requisicion")
    requisiciones = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("lista_requi.html", requisiciones=requisiciones)





# Ruta para agregar la requisición
@app.route('/requisicion_agr')
def requisicion_agregar():
    return render_template("requisicion_agr.html")

@app.route('/requisicion_agr', methods=['POST'])
def agregar_requisicion():
    folio = request.form['folio']
    fechaElab = request.form['fechaElab']
    fechaRecluta = request.form['fechaRecluta']
    fechaInicVac = request.form['fechaInicVac']
    motivoRequisicion = request.form['motivoRequisicion']
    motivoEspecifique = request.form['motivoEspecifique']
    tipoVacante = request.form['tipoVacante']
    nomSolicita = request.form['nomSolicita']
    idPuesto = request.form['idPuesto']
    idArea = request.form['idArea']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO requisicion (folio, fechaElab, fechaRecluta, fechaInicVac, motivoRequisicion, motivoEspecifique, tipoVacante, nomSolicita, idPuesto, idArea) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (folio, fechaElab, fechaRecluta, fechaInicVac, motivoRequisicion, motivoEspecifique, tipoVacante, nomSolicita, idPuesto, idArea))
    conn.commit()

    cursor.execute("SELECT * FROM requisicion WHERE idRequisicion = LAST_INSERT_ID()")
    requisicion = cursor.fetchone()

    cursor.close()
    conn.close()
    
    return render_template("requisicion.html", requisicion=requisicion)


@app.route('/aceptar_requisicion', methods=['POST'])
def aceptar_requisicion():
    requisicion_id = request.form['idRequisicion']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute("UPDATE requisicion SET idPuesto = 1, autorizada = 1 WHERE idRequisicion = %s", (requisicion_id,))
    conn.commit()

    cursor.execute("SELECT * FROM requisicion WHERE idRequisicion = %s", (requisicion_id,))
    requisicion = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("requisicion.html", requisicion=requisicion)


@app.route('/cont_p/<string:idC>', methods=['GET'])
def contrato_p(idC):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select p.idPuesto from puesto p, candidato c where p.idPuesto = c.idPuesto and c.idCandidato = %s', (idC))
    idP = cursor.fetchone()
    
    cursor.execute('select c.idCandidato, c.nombre, p.nomPuesto from candidato c, puesto p where c.idPuesto = p.idPuesto')
    r = cursor.fetchall()

    cursor.execute('select nombre, edad, sexo, CURP, RFC, domCalle, domNumExtInt, domColonia, correoE, tel1, tel2 '
            'from candidato where idCandidato = %s', (idC))
    datos = cursor.fetchone()

    cursor.execute('select puestoJefeSup, nomPuesto, codPuesto, jornada, remunMensual, prestaciones, descripcionGeneral, funciones, experiencia, '
                'conocimientos, manejoEquipo, reqFisicos, reqPsicologicos, condicionesTrabajo, responsabilidades from puesto where idPuesto = %s', (idP,))
    dato = cursor.fetchone()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos1 = cursor.fetchone()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, candidato b where a.idEstadoCivil = b.idEstadoCivil and b.idCandidato = %s', (idC))
    datos2 = cursor.fetchone()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, candidato b where a.idEscolaridad = b.idEscolaridad and b.idCandidato = %s', (idC))
    datos3 = cursor.fetchone()

    cursor.execute('select a.idGradoAvance, a.descripcion from grado_avance a, candidato b where a.idGradoAvance = b.idGradoAvance and b.idCandidato = %s', (idC))
    datos4 = cursor.fetchone()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, candidato b where a.idCarrera = b.idCarrera and b.idCandidato = %s', (idC))
    datos5 = cursor.fetchone()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                    'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos6 = cursor.fetchone()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                    'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos7 = cursor.fetchone()

    cursor.execute('select p.nomPuesto, a.descripcion, p.puestoJefeSup, p.jornada, p.funciones, p.responsabilidades, p.remunMensual,' 
                    'p.prestaciones from puesto p, area a where a.idArea = p.idArea and idPuesto = %s', (idP))
    clausu1 = cursor.fetchone()

    cursor.execute('select r.fechainicVac, c.nombre, p.nomPuesto from puesto p, requisicion r, candidato c where r.idRequisicion = c.idRequisicion and ' 
                    'p.idPuesto = c.idPuesto and c.idCandidato = %s', (idC))
    clausu2 = cursor.fetchone()

    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 15, 'CONTRATO LABORAL', 0, 1, 'C')

        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

        def chapter_title(self, title):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, title, 0, 1, 'L')
            self.ln(5)

        def chapter_body(self, body):
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 7, body)
            self.ln()

        def chapter_datos(self, body):
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 3, body)
            self.ln()

    # Create instance of FPDF class
    pdf = PDF()

    # Add a page
    pdf.add_page()

    # Set title
    pdf.set_font('Arial', 'B', 16)

    # Add the company section
    pdf.chapter_title('DATOS DE LA EMPRESA')
    empresa = [
        'Nombre: Swift Market',
        'Ubicacion: Av. Perseo 301, Ptimo Verdad Inegi',
        'Codigo Postal: 20267',
        'Municipio: Aguascalientes',
        'Estado: Aguascalientes',
        'Detalles: Se dedica a la venta de productos'
    ]
    for item in empresa:
        pdf.chapter_datos(item)

    # Add a line break
    pdf.ln(10)

    # Add the job section
    pdf.chapter_title('DATOS DEL PUESTO')
    puesto = [
        f'Supervisor: {dato[0]}',
        f'Nombre del puesto: {dato[1]}',
        f'Código del puesto: {dato[2]}',
        f'Area: {datos1[1]}',
        f'Jornada: {dato[3]}',
        f'Remuneracion mensual: {dato[4]}',
        f'Prestaciones: {dato[5]}',
        'Fecha de pago: 30 de cada mes',
        'Forma de pago: Efectivo',
        f'Descripcion general: {dato[6]}',
        'Estancia: 3 meses',
        'Vacaciones: No',
        'Lugar de trabajo: Empresa',
        'Duración de contrato: 3 meses',
        f'Funciones: {dato[7]}',
        f'Experiencia: {dato[8]}',
        f'Conocimientos: {dato[9]}',
        f'Manejo de equipo: {dato[10]}',
        f'Requisitos fisicos: {dato[11]}',
        f'Requisitos psicologicos: {dato[12]}',
        f'Idiomas: {datos6[2]}',
        f'habilidades: {datos7[2]}',
        f'Condiciones de trabajo: {dato[13]}',
        f'Responsabilidades: {dato[14]}'
    ]
    for item in puesto:
        pdf.chapter_datos(item)

    # Add a line break
    pdf.ln(10)

    # Add the worker section
    pdf.chapter_title('DATOS DEL TRABAJADOR')
    trabajador = [
        f'Nombre: {datos[0]}',
        f'Edad: {datos[1]}',
        f'Sexo: {datos[2]}',
        f'CURP: {datos[3]}',
        f'RFC: {datos[4]}',
        f'Domicilio: {datos[5]} {datos[6]} {datos[7]}',
        f'Correo electronico: {datos[8]}',
        f'Telefono 1: {datos[9]}',
        f'Telefono 2: {datos[10]}',
        f'Estado civil: {datos2[1]}',
        f'Escolaridad: {datos3[1]}',
        f'Grado de avance: {datos4[1]}',
        f'Carrera: {datos5[1]}'
    ]
    for item in trabajador:
        pdf.chapter_datos(item)

    # Add a line break
    pdf.ln(10)

    # Add clauses section
    pdf.chapter_title('CLÁUSULAS')
    clausulas = [
        f'1. Al firmar esta dispuesto a trabajar en la empresa "Swift Market" ubicada en Av. Perseo 301, Ptimo Verdad Inegi, en el puesto de {clausu1[0]} en el area de Area Name a cargo del {clausu1[1]}, durante la jornada de {clausu1[2]}, en la cual va a tener que {clausu1[3]} y sus responsabilidades seran {clausu1[4]}, al hacer esto se le dara un pago de {clausu1[5]} al mes, con prestaciones {clausu1[7]}.',
        f'2. Citando la Ley Federal de Trabajo Articulo 38-39 se establece que la empresa se compromete a cumplir con la capacitacion inicial desde el dia {clausu2[0]} del candidato {clausu2[1]} para el puesto {clausu2[2]}, capacitando y adiestrando todas sus funciones y responsabilidades que son requeridas para el puesto de forma segura y saludable para ambas partes del contrato.',
        '3. La empresa se compromete a darle todo el equipo, conocimientos y ambiente que necesita a el trabajador para realizar su trabajo en la empresa. Las lecciones de la capacitacion se dara dentro de la empresa con su respectivo supervisor en el horario de la jornada.',
        '4. La trabajador se debe comprometer a asistir a todas las lecciones de su capacitacion, participar activamente y lleavr a cabo todo lo aprendido de estas en su laboral.',
        '5. En caso de cualquier conflicto que suceda entre empleados ya sea fuera o dentro de la empresa tendra que ser informado a recursos humanos para poder llegar a la causa del problema y a una solucion para la sana convivencia en el area de trabajo y en el horario de trabajo. En caso de que el problema sea muy grave se tomaran medidas con el trabajador y su contrato puede terminar antes.',
        '6. Cualquier cosa echa dentro de la empresa que no este relacionada a su trabajo le pertenecera a la misma empresa.',
        '7. Mientras trabaje en la empresa no podra hacer ningun trabajo ya sea externo o propio el cual sea competencia con la empresa.',
        '8. Al finalizar el contrato, su supervisor se encargara de dar un imforme del progreso y rendimiento en el periodo que estuvo en la empresa y se decidira si se le ofrece un nuevo contrato.',
        '9. Despues de firmar ambas partes esta aceptando tener alta confidencialidad sobre la empresa y lo que pase dentro de la misma incluyendo datos o estadisticas de los ingresos de la empresa.'
    ]
    for item in clausulas:
        pdf.chapter_body(item)

    # Add signatures section
    pdf.ln(20)
    pdf.cell(90, 10, '_____________________')
    pdf.cell(90, 10, '_____________________')
    pdf.ln(10)
    pdf.cell(90, 10, 'Firma del supervisor')
    pdf.cell(90, 10, 'Firma del trabajador')

    # Output the PDF
    # Especificar una ruta absoluta para guardar el archivo PDF
    archivo = "Contrato laboral.pdf"
    output_path = os.path.join(os.path.expanduser('~'), 'Desktop', archivo)
    webbrowser.open(output_path)
    pdf.output(output_path)
    print(f'Nombre:{archivo}')
    print(f'Archivo PDF guardado en {output_path}')
    return redirect(url_for('candidatos'))


#Codigo de Python del Equipo2

#Renderizado para las Vacantes Equipo2
@app.route('/vacantes')
def vacantes():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    return render_template("vacantes.html", pue = datos, dat='   ', catArea = '   ', catEdoCivil = '   ', catEscolaridad = '   ',
                           catGradoAvance = '    ', catCarrera = '    ', catIdioma = ' ', catHabilidad = ' ')

#Metodo para mostrar los datos en la publicacion de Vacantes Equipo2
@app.route('/vacantes_publ/<string:idV>', methods=['GET'])
def vacantes_publ(idV):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
            'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
            'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idV))
    dato = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idV))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s', (idV))
    datos2 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idV))
    datos3 = cursor.fetchall()

    cursor.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s', (idV))
    datos4 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idV))
    datos5 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idV))
    datos6 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idV))
    datos7 = cursor.fetchall()
    return render_template("pub_vacantes.html", pue = datos, dat=dato[0], catArea=datos1[0], catEdoCivil=datos2[0], catEscolaridad=datos3[0],
                           catGradoAvance=datos4[0], catCarrera=datos5[0], catIdioma=datos6, catHabilidad=datos7)

#Renderizado para la Publicacion de Vacantes Equipo2
@app.route('/pub_vacantes')
def pub_vacantes():
    return render_template("pub_vacantes.html")

@app.route('/vacantes_pub')
def vacantes_pub():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    return render_template("vacantes.html", pue = datos, dat='   ', catArea = '   ', catEdoCivil = '   ', catEscolaridad = '   ',
                           catGradoAvance = '    ', catCarrera = '    ', catIdioma = ' ', catHabilidad = ' ')

#Funcion para Generar un Anuncio de Vacantes por PDF Equipo2
#Libreria Usada WeasyPrint (Instalacion: pip install weasyprint       Despues se instalaran y configurara la dependencia)
@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Obtener datos del formulario
    data = {
        "nomPuesto": request.form['nomPuesto'],
        "codPuesto": request.form['codPuesto'],
        "idArea": request.form['idArea'],
        "puestoJefeSup": request.form['puestoJefeSup'],
        "jornada": request.form['jornada'],
        "remunMensual": request.form['remunMensual'],
        "prestaciones": request.form['prestaciones'],
        "descripcionGeneral": request.form['descripcionGeneral'],
        "funciones": request.form['funciones'],
        "edad": request.form['edad'],
        "sexo": request.form['sexo'],
        "idEstadoCivil": request.form['idEstadoCivil'],
        "idEscolaridad": request.form['idEscolaridad'],
        "idGradoAvance": request.form['idGradoAvance'],
        "idFormaPubl": request.form['idFormaPubl']
    }

    # Renderizar plantilla HTML con los datos
    rendered_html = render_template('pdf.html', data=data)

    # Convertir el HTML a PDF
    pdf = HTML(string=rendered_html).write_pdf()

    # Guardar el PDF en el sistema de archivos
    pdf_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'vacante.pdf')
    with open(pdf_path, 'wb') as f:
        f.write(pdf)

    # Devolver el PDF como respuesta
    return send_file(pdf_path, as_attachment=True, download_name='vacante.pdf')

#Fin del codigo del Equipo2
#examen psicometrico
@app.route('/examen')
def examen():
    return render_template('examen.html')
 
@app.route('/examen_enviar', methods=['POST'])
def examen_enviar():
    if request.method == 'POST':
        nom=request.form['nombre']
        p1=request.form['p1']
        p2=request.form['p2']
        p3=request.form['p3']
        p4=request.form['p4']
        p5=request.form['p5']
        p6=request.form['p6']
        p7=request.form['p7']
        p8=request.form['p8']
        p9=request.form['p9']
        p10=request.form['p10']
        p11=request.form['p11']
        p12=request.form['p12']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO examen (nombre, preg1, preg2, preg3, preg4, preg5, preg6, preg7, preg8, preg9, preg10, preg11, preg12) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (nom,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12))
        conn.commit()
    return redirect(url_for('crud_examen'))

@app.route('/crud_examen')
def crud_examen():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('SELECT idExamen, nombre FROM examen order by idExamen')
    datos = cursor.fetchall()
    return render_template('examen_crudr.html', comentarios=datos)

@app.route('/examen_borrar/<string:id>')
def examen_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM examen WHERE idExamen={0}'.format(id))
    conn.commit()
    return redirect(url_for('crud_examen'))

@app.route('/examen_calificar/<string:id>')
def examen_calificar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idExamen, nombre, preg1, preg2, preg3, preg4, preg5, preg6, preg7, preg8, preg9, preg10, preg11, preg12 FROM examen WHERE idExamen=%s", (id))
    dato=cursor.fetchone()
    return render_template('califica_examen.html', com=dato)

@app.route('/examen_revisado/<string:id>', methods=['POST'])
def examen_revisado(id):
    if request.method == 'POST':
        cal1=int(request.form['preg1'])
        cal2=int(request.form['preg2'])
        cal3=int(request.form['preg3'])
        cal4=int(request.form['preg4'])
        cal5=int(request.form['preg5'])
        cal6 = int(request.form['preg6'])
        cal7=int(request.form['preg7'])
        cal8=int(request.form['preg8'])
        cal9=int(request.form['preg9'])
        cal10=int(request.form['preg10'])
        cal11=int(request.form['preg11'])
        cal12=int(request.form['preg12'])
        cali=cal1+cal2+cal3+cal4+cal5+cal6+cal7+cal8+cal9+cal10+cal11+cal12
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('SELECT nombre, preg1, preg2, preg3, preg4, preg5, preg6, preg7, preg8, preg9, preg10, preg11, preg12 FROM examen WHERE idExamen=%s',(id))
        dato = cursor.fetchone()
        if dato:
            nombre, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12 = dato
            cursor.execute('DELETE FROM examen WHERE idExamen=%s',(id,))
            cursor.execute('INSERT INTO calificaciones (nombre, calificacion, preg1, preg2, preg3, preg4, preg5, preg6, preg7, preg8, preg9, preg10, preg11, preg12) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (nombre, cali, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12))
            conn.commit()
    return redirect(url_for('calificaciones'))

@app.route('/calificaciones')
def calificaciones():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('SELECT idCalificacion, nombre, calificacion FROM calificaciones order by idCalificacion')
    datos=cursor.fetchall()
    return render_template('calificaciones.html', comentarios=datos)

@app.route('/calificacion_borrar/<string:id>')
def calificacion_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM calificaciones WHERE idCalificacion=%s', (id))
    conn.commit()
    return redirect(url_for('calificaciones'))

@app.route('/calificacion_detalles/<string:id>')
def calc_detalles(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('SELECT idCalificacion, nombre, preg1, preg2, preg3, preg4, preg5, preg6, preg7, preg8, preg9, preg10, preg11, preg12, calificacion FROM calificaciones WHERE idCalificacion=%s',(id))
    datos =cursor.fetchone()
    return render_template('detalle_cali.html', com=datos)

@app.route('/regreso')
def regreso():
    return redirect(url_for('calificaciones'))
#fin equipo 5
if __name__ == "__main__":
    app.run(debug=True)



