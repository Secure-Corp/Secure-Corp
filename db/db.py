import re
import pymysql

class CBD():

    def __init__(self):
        try:
            #Crea una conexion con los datos que se recolectaron de XAMPP
            self.conn = pymysql.connect(host='localhost', user=self.usuarioXampp, passwd='', port=self.puertoXampp, db="rh3")
            self.cursor = self.conn.cursor()
            print("\nConexión exitosa\n")

        except pymysql.Error as err:
            self.conn = pymysql.connect(host='localhost', user=self.usuarioXampp, passwd='', port=self.puertoXampp)
            self.cursor = self.conn.cursor()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS rh3")
            self.cursor.execute("USE rh3")
            print("\nCreación exitosa\n")
        

    # Detectar puerto y usuario de XAMPP
    def detectarPuertosXampp(rutaXampp='C:/xampp/mysql/bin/my.ini'):
        try:
            with open(rutaXampp, 'r') as archivo:
                contenido = archivo.read()

            # el re.search sirve para detectar los numeros del 0 al 9 con la sentencia de \d
            resultado_puerto = re.search(r'port[ ]*=[ ]*(\d+)', contenido)
            if resultado_puerto:
                puerto = int(resultado_puerto.group(1))  

            else:
                print("No hay puerto predeterminado")
                puerto =  None
            
            # el re.search sirve para detectar los caracteres alfanumericos con la sentencia de \w
            # En caso de no encontrar un usuario se llenara con un root
            resultado_usuario = re.search(r'user[ ]*=[ ]*(\w+)', contenido)
            if resultado_usuario:
                usuario = resultado_usuario.group(1)
            else:
                print("\nNo se encontró un nombre de usuario")
                usuario = "root"

            return puerto, usuario

        # Por si no se encontro el archivo en la ruta mencionada 
        except FileNotFoundError:
            print(f"No se encontro Xampp en la ruta {rutaXampp}")
            return None, None


    puertoXampp, usuarioXampp = detectarPuertosXampp()
    if puertoXampp:
        print(f"\nEl puerto de MySQL es {puertoXampp}")
        print(f"El nombre de usuario de MySQL es {usuarioXampp}")
    else:
        print("No se pudo encontrar el puerto de Xampp")

#Empezamos a crear todas las tablas junto con los datos de nuestra base de datos y en caso de encontrrar un error lo mostrara en consola
    def crearTablaAgcuso(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists agcuso (idagcu int(11) not null AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50) NOT NULL, descripcion VARCHAR(120) NOT NULL, completado INT(3) NOT NULL, idusuario INT(11) NOT NULL)")

        except pymysql.Error as err:
            print("\nError al crear la tabla agcuso: {0}".format(err))

    def crearTablaArea(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists area (idArea int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, descripcion varchar(60) NOT NULL)")
            self.cursor.execute("SELECT COUNT(*) FROM area")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO area (descripcion) VALUES ('DIRECCION GENERAL')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO area (descripcion) VALUES ('ADMINISTRACION Y RECURSOS HUMANOS')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO area (descripcion) VALUES ('PRODUCCION')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO area (descripcion) VALUES ('FINANZAS Y CONTABILIDAD')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO area (descripcion) VALUES ('MERCADOTECNIA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO area (descripcion) VALUES ('SERVICIOS DE VIGILANCIA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO area (descripcion) VALUES ('SERVICIOS DE PROTECCION PERSONAL')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO area (descripcion) VALUES ('PROTECCION PERSONAL')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO area (descripcion) VALUES ('SEGURIDAD ELECTRONICA')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla area: {0}".format(err))

    def crearTablaCalificaciones(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists calificaciones (idCalificacion int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, nombre varchar(225) not null, calificacion int(11) NOT NULL, preg1 varchar(250) NOT NULL, preg2 varchar(250) NOT NULL, preg3 varchar(250) NOT NULL, preg4 varchar(250) NOT NULL, preg5 varchar(250) NOT NULL, preg6 varchar(250) NOT NULL, preg7 varchar(250) NOT NULL, preg8 varchar(250) NOT NULL, preg9 varchar(250) NOT NULL, preg10 varchar(250) NOT NULL, preg11 varchar(250) NOT NULL, preg12 varchar(250) NOT NULL, rfc varchar(20) NOT NULL, aprobado varchar(20) NOT NULL, observaciones varchar(200) NOT NULL)")
            
        except pymysql.Error as err:
            print("\nError al crear la tabla calificaciones: {0}".format(err))

    def crearTablaCandidato(self):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS candidato (idCandidato int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, idVacante int(11) NOT NULL, idRequisicion int(11) NOT NULL, idPuesto int(11) NOT NULL, CURP varchar(30) NOT NULL, RFC varchar(20) NOT NULL, nombre varchar(40) NOT NULL, domCalle varchar(40) NOT NULL, domNumExtInt varchar(30) NOT NULL, domColonia varchar(40) NOT NULL, tel1 varchar(20) NOT NULL, tel2 varchar(20) NOT NULL, correoE varchar(40) NOT NULL, edad int(11) NOT NULL, sexo varchar(10) NOT NULL, idEstadoCivil int(11) NOT NULL, idEscolaridad int(11) NOT NULL, idGradoAvance int(11) NOT NULL, idCarrera int(11) NOT NULL, entrevSelecReq tinyint(4) NOT NULL, entrevSelecPresen tinyint(4) NOT NULL, entrevSelecResult varchar(40) NOT NULL, evalMedicaReq tinyint(4) NOT NULL, evalMedicaPresen tinyint(4) NOT NULL, evalMedicaResult varchar(40) NOT NULL, evalPsicolgReq tinyint(4) NOT NULL, evalPsicologPresen tinyint(4) NOT NULL, evalPsicologResult varchar(40) NOT NULL, evalPsicometReq tinyint(4) NOT NULL, evalPsicometPresene tinyint(4) NOT NULL, evalPsicometResult varchar(40) NOT NULL, evalTecnicaReq tinyint(4) NOT NULL, evalTecnicaPresen tinyint(4) NOT NULL, evalTecnicaResult varchar(41) NOT NULL, evalConocReq tinyint(4) NOT NULL, evalConocPresen tinyint(4) NOT NULL, evalConocResult varchar(40) NOT NULL, entrevFinalReq tinyint(4) NOT NULL, entrevFinalPresen tinyint(4) NOT NULL, entrevFinalResul varchar(40) NOT NULL, aprobado varchar(30) NOT NULL, calificacion varchar(30) NOT NULL)")
            self.cursor.execute("SELECT COUNT(*) FROM candidato")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO candidato (idVacante, idRequisicion, idPuesto, CURP, RFC, nombre, domCalle, domNumExtInt, domColonia, tel1, tel2, correoE, edad, sexo, idEstadoCivil, idEscolaridad, idGradoAvance, idCarrera, entrevSelecReq, entrevSelecPresen, entrevSelecResult, evalMedicaReq, evalMedicaPresen, evalMedicaResult, evalPsicolgReq, evalPsicologPresen, evalPsicologResult, evalPsicometReq, evalPsicometPresene, evalPsicometResult, evalTecnicaReq, evalTecnicaPresen, evalTecnicaResult, evalConocReq, evalConocPresen, evalConocResult, entrevFinalReq, entrevFinalPresen, entrevFinalResul, aprobado, calificacion) VALUES (1, 1, 1, 'ROGH760106MASDML03', 'FDGEJD6485933', 'Jose', 'Pedro Ascencio', '233', 'Morelos I', '453-454-6754', '235-097-6789', 'jjose@gmail.com', 33, 'Indistinto', 1, 2, 1, 1, 0, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 'No requerida/No presentada', 'No requerida/No presentada')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO candidato (idVacante, idRequisicion, idPuesto, CURP, RFC, nombre, domCalle, domNumExtInt, domColonia, tel1, tel2, correoE, edad, sexo, idEstadoCivil, idEscolaridad, idGradoAvance, idCarrera, entrevSelecReq, entrevSelecPresen, entrevSelecResult, evalMedicaReq, evalMedicaPresen, evalMedicaResult, evalPsicolgReq, evalPsicologPresen, evalPsicologResult, evalPsicometReq, evalPsicometPresene, evalPsicometResult, evalTecnicaReq, evalTecnicaPresen, evalTecnicaResult, evalConocReq, evalConocPresen, evalConocResult, entrevFinalReq, entrevFinalPresen, entrevFinalResul, aprobado, calificacion) VALUES (1, 1, 1, 'ROML551119HASDCR08', 'DJF84093JFJ4', 'Juan', 'Jefes Insurgentes', '278', 'Fundadores', '342-322-1145', '347-657-5433', 'jjuan@outlook.com', 30, 'Indistinto', 3, 2, 3, 1, 0, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 'No requerida/No presentada', 'No requerida/No presentada')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO candidato (idVacante, idRequisicion, idPuesto, CURP, RFC, nombre, domCalle, domNumExtInt, domColonia, tel1, tel2, correoE, edad, sexo, idEstadoCivil, idEscolaridad, idGradoAvance, idCarrera, entrevSelecReq, entrevSelecPresen, entrevSelecResult, evalMedicaReq, evalMedicaPresen, evalMedicaResult, evalPsicolgReq, evalPsicologPresen, evalPsicologResult, evalPsicometReq, evalPsicometPresene, evalPsicometResult, evalTecnicaReq, evalTecnicaPresen, evalTecnicaResult, evalConocReq, evalConocPresen, evalConocResult, entrevFinalReq, entrevFinalPresen, entrevFinalResul, aprobado, calificacion) VALUES (1, 1, 1, 'ARMO451209HASGTR07', 'FGD8665GFH7F5', 'Pedro', 'Artillero Mier', '348', 'Casa Blanca', '392-466-0145', '390-432-4654', 'ppedro@outlook.com', 45, 'Indistinto', 2, 1, 2, 1, 0, 0, 'NO APLICA/NO PRESENTADA', 1, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 1, 0, 'NO APLICA/NO PRESENTADA', 0, 0, 'NO APLICA/NO PRESENTADA', 1, 0, 'NO APLICA/NO PRESENTADA', 1, 0, 'NO APLICA/NO PRESENTADA', 'No requerida/No presentada', 'No requerida/No presentada')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla candidato: {0}".format(err))

    def crearTablaCarrera(self):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS carrera (idCarrera int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, descripcion varchar(50) NOT NULL)")
            self.cursor.execute("SELECT COUNT(*) FROM carrera")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('NO APLICA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('ADMINISTRACION DE EMPRESAS')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('ADMINISTRACIÓN DE PRODUCCIÓN Y SERVICIOS')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('ADMINISTRACIÓN FINANCIERA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('LICENCIATURA EN SEGURIDAD INDUSTRIAL')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('COMERCIO ELECTRONICO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('ADMINISTRACION DE RIESGOS Y SEGUROS')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('CONTADOR ')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('INSPECCION SANITARIA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('LICENCIATURA EN ESTUDIOS AMBIENTALES')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('LOGISTICA EMPRESARIAL')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('MERCADOTECNIA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('SISTEMAS COMPUTACIONALES Y AFINES')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('INDUSTRIAL')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('ELECTRICA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('ROBOTICA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('RELACIONES INDUSTRIALES')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('PSICOLOGIA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('ELECTRONICA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO carrera (descripcion) VALUES ('GESTION EMPRESARIAL')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla carrera: {0}".format(err))

    def crearTablaCompletadas(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists completadas (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, descripcion varchar(2) NOT NULL)")
            self.cursor.execute("SELECT COUNT(*) FROM completadas")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO completadas (descripcion) VALUES ('si')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO completadas (descripcion) VALUES ('no')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla completadas: {0}".format(err))

    def crearTablaCursos(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists cursos (idcursos int(11) not null auto_increment PRIMARY KEY, nombre varchar(50) not null, descripcion varchar(120) not null)")
            self.cursor.execute("SELECT COUNT(*) FROM cursos")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO cursos (nombre, descripcion) VALUES ('SEGURIDAD CONTRA INCENDIOS','Qué hacer en caso de incendios')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO cursos (nombre, descripcion) VALUES ('USO SEGURO DE LA MAQUINARIA','Para saber usar maquinas peligrosas')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO cursos (nombre, descripcion) VALUES ('GESTION DE RIESGOS','Conocer, identificar y tratar riesgos')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO cursos (nombre, descripcion) VALUES ('EQUIPO DE PROTECCION PERSONAL','Conocer el uso de proteccion personal')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO cursos (nombre, descripcion) VALUES ('TRATAR CON CLIENTES DIFICILES','Saber tratar con personas dificiles o molestas')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla cursos: {0}".format(err))

    def crearTablaDoctoSolic(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists docto_solic (idDoctoSolic int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, descripcion varchar(70) not null, original varchar(2) not null, numCopias int(5) not null)")
            self.cursor.execute("SELECT COUNT(*) FROM docto_solic")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Solicitud de empleo', 'SI', 1)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('CURRICULUM VITAE con fotografía', 'SI', 1)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Carta de presentación', 'SI', 1)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Carta de recomendación', 'SI', 1)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Comprobante de domicilio reciente', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Acta de nacimiento', 'SI', 1)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Número del seguro social', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('CURP', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Credencial para votar', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Licencia automovilista', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Licencia chofer', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Certificado Carrera Comercial o Técnica', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Certificado Preparatoria o Equivalente', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Certificado Licenciatura o Equivalente', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Constancia de Estudios', 'SI', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Carta de Pasante Carrera Técnica', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Carta de Pasante Licenciatura', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Carta de Pasante Posgrado', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Cédula Profesional', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Título Licenciatura', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Título Posgrado', 'NO', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Certificado Médico', 'SI', 2)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO docto_solic (descripcion, original, numCopias) VALUES ('Antecedentes No penales', 'Si', 1)")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla docto_solic: {0}".format(err))

    def crearTablaEmpleado(self):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS `empleado` (`idEmpleado` int(11) NOT NULL AUTO_INCREMENT,`codPuesto` varchar(15) NOT NULL,`idArea` int(11) NOT NULL,`nomEmpleado` varchar(50) NOT NULL,`jornada` varchar(70) NOT NULL,`descripcionGeneral` varchar(250) NOT NULL,`edad` varchar(50) NOT NULL,`sexo` varchar(15) NOT NULL,`idEstadoCivil` int(11) NOT NULL,`idEscolaridad` int(11) NOT NULL,`idGradoAvance` int(11) NOT NULL,`idCarrera` int(11) NOT NULL,`experiencia` varchar(70) NOT NULL,`conocimientos` varchar(70) NOT NULL,`manejoEquipo` varchar(70) NOT NULL,`responsabilidades` varchar(70) NOT NULL,PRIMARY KEY (`idEmpleado`),KEY `idEscolaridad` (`idEscolaridad`),KEY `idEstadoCivil` (`idEstadoCivil`),KEY `idGradoAvance` (`idGradoAvance`),KEY `idCarrera` (`idCarrera`),KEY `area` (`idArea`)) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;")
            self.cursor.execute("SELECT COUNT(*) FROM empleado")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO `empleado` (`idEmpleado`, `codPuesto`, `idArea`, `nomEmpleado`, `jornada`, `descripcionGeneral`, `edad`, `sexo`, `idEstadoCivil`, `idEscolaridad`, `idGradoAvance`, `idCarrera`, `experiencia`, `conocimientos`, `manejoEquipo`, `responsabilidades`) VALUES(1, 'V009', 5, 'Carlos Julian ', 'LUNES A VIERNES', 'VENDER', '34 AÑOS', 'Hombre', 1, 3, 2, 2, '2 AÑOS', 'VENTAS', 'DE COMPUTO',  'INVENTARIO' ), (3, 'v0008', 3, 'Aranza Mendoza',  'LUNES A VIERNES', 'trabajar', '21 AÑOS', 'Indistinto', 1, 2, 2, 1, '2 AÑOS', 'VENTAS', 'DE COMPUTO',  'INVENTARIO')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla empleado: {0}".format(err))

    def crearTablaEscolaridad(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists escolaridad (idEscolaridad int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, descripcion varchar(50) NOT NULL)")
            self.cursor.execute("SELECT COUNT(*) FROM escolaridad")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO escolaridad (descripcion) VALUES ('NO APLICA / NO REQUERIDA ')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO escolaridad (descripcion) VALUES ('PREPARATORIA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO escolaridad (descripcion) VALUES ('CARRERA TÉCNICA O COMERCIAL')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO escolaridad (descripcion) VALUES ('BACHILLERATO TÉCNICO O ESPECIALIZADO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO escolaridad (descripcion) VALUES ('TÉCNICO SUPERIOR UNIVERSITARIO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO escolaridad (descripcion) VALUES ('LICENCIATURA / INGENIERÍA / PROFESIONAL')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO escolaridad (descripcion) VALUES ('MAESTRIA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO escolaridad (descripcion) VALUES ('DOCTORADO')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla escolaridad: {0}".format(err))

    def crearTablaEstadoCivil(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists estado_civil (idEstadoCivil int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, descripcion varchar(50) NOT NULL)")
            self.cursor.execute("SELECT COUNT(*) FROM estado_civil")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO estado_civil (descripcion) VALUES ('INDISTINTO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO estado_civil (descripcion) VALUES ('SOLTERO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO estado_civil (descripcion) VALUES ('CASADO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO estado_civil (descripcion) VALUES ('UNION LIBRE')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO estado_civil (descripcion) VALUES ('VIUDO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO estado_civil (descripcion) VALUES ('DIVORCIADO')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla estado_civil: {0}".format(err))

    def crearTablaExamen(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists examen (idExamen int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, nombre varchar(70) NOT NULL, preg1 varchar(250) NOT NULL, preg2 varchar(250) NOT NULL, preg3 varchar(250) NOT NULL, preg4 varchar(250) NOT NULL, preg5 varchar(250) NOT NULL, preg6 varchar(250) NOT NULL, preg7 varchar(250) NOT NULL, preg8 varchar(250) NOT NULL, preg9 varchar(250) NOT NULL, preg10 varchar(250) NOT NULL, preg11 varchar(250) NOT NULL, preg12 varchar(250) NOT NULL, rfc varchar(20) NOT NULL)")
        except pymysql.Error as err:
            print("\nError al crear la tabla examen: {0}".format(err))

    def crearTablaGradoA(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists grado_avance (idGradoAvance int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, descripcion varchar(45) NOT NULL)")
            self.cursor.execute("SELECT COUNT(*) FROM grado_avance")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO grado_avance (descripcion) VALUES ('NO APLICA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO grado_avance (descripcion) VALUES ('CURSANDO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO grado_avance (descripcion) VALUES ('TERMINADO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO grado_avance (descripcion) VALUES ('INCONCLUSO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO grado_avance (descripcion) VALUES ('PASANTE')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO grado_avance (descripcion) VALUES ('TITULADO')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla grado_avance: {0}".format(err))

    def crearTablaHabilidad(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists habilidad (idHabilidad int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, descripcion varchar(150) NOT NULL)")
            self.cursor.execute("SELECT COUNT(*) FROM habilidad")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO habilidad (descripcion) VALUES ('NO REQUERIDAS')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO habilidad (descripcion) VALUES ('FACILIDAD DE PALABRA')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO habilidad (descripcion) VALUES ('MANEJO DE CONFLICTOS')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO habilidad (descripcion) VALUES ('CAPACIDAD PARA TRABAJAR BAJO PRESION')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO habilidad (descripcion) VALUES ('CAPACIDAD DE TRABAJO EN EQUIPO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO habilidad (descripcion) VALUES ('TOMA DE DECISIONES')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO habilidad (descripcion) VALUES ('PENSAMIENTO CREATIVO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO habilidad (descripcion) VALUES ('PENSAMIENTO CRITICO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO habilidad (descripcion) VALUES ('MANEJO DE EMOCIONES')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO habilidad (descripcion) VALUES ('PROACTIVIDAD')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO habilidad (descripcion) VALUES ('PROFESIONALIDAD')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO habilidad (descripcion) VALUES ('ESCUCHA ACTIVA')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla habilidad: {0}".format(err))

    def crearTablaIdioma(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists idioma (idIdioma int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, descripcion varchar(50) NOT NULL)")
            self.cursor.execute("SELECT COUNT(*) FROM idioma")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO idioma (descripcion) VALUES ('NO REQUERIDO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO idioma (descripcion) VALUES ('INGLES BASICO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO idioma (descripcion) VALUES ('INGLES INTERMEDIO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO idioma (descripcion) VALUES ('INGLES AVANZADO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO idioma (descripcion) VALUES ('JAPONES BASICO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO idioma (descripcion) VALUES ('JAPONES CONVERSACIONAL')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO idioma (descripcion) VALUES ('JAPONES ESCRITO Y CONVERSACIONAL')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO idioma (descripcion) VALUES ('ALEMAN AVANZADO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO idioma (descripcion) VALUES ('ALEMAN BASICO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO idioma (descripcion) VALUES ('FRANCES AVANZADO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO idioma (descripcion) VALUES ('FRANCES INTERMEDIO')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO idioma (descripcion) VALUES ('FRANCES BASICO')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla idioma: {0}".format(err))

    def crearTablaMedioPub(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists mediopublic (idMedioPublic int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, descripcion varchar(70) NOT NULL)")
            self.cursor.execute("SELECT COUNT(*) FROM mediopublic")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO mediopublic (descripcion) VALUES ('Convocatoria en áreas estratégicas de la empresa')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO mediopublic (descripcion) VALUES ('Sitio web de la empresa')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO mediopublic (descripcion) VALUES ('Servicio estatal de empleo')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO mediopublic (descripcion) VALUES ('Redes sociales para empleo')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO mediopublic (descripcion) VALUES ('Agencia particular de empleo')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO mediopublic (descripcion) VALUES ('Radio')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO mediopublic (descripcion) VALUES ('Televisión')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO mediopublic (descripcion) VALUES ('Periódico Digital')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO mediopublic (descripcion) VALUES ('Carteles/Espectaculares')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla mediopublic: {0}".format(err))

    def crearTablaPuesto(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists puesto (idPuesto int(11) NOT NULL AUTO_INCREMENT, codPuesto varchar(15) NOT NULL, idArea int(11) NOT NULL, nomPuesto varchar(50) NOT NULL, puestoJefeSup varchar(50) NOT NULL, jornada varchar(70) NOT NULL, remunMensual int(11) NOT NULL, prestaciones varchar(70) NOT NULL, descripcionGeneral varchar(250) NOT NULL, funciones varchar(250) NOT NULL, edad varchar(50) NOT NULL, sexo varchar(15) NOT NULL, idEstadoCivil int(11) NOT NULL, idEscolaridad int(11) NOT NULL, idGradoAvance int(11) NOT NULL, idCarrera int(11) NOT NULL, experiencia varchar(70) NOT NULL, conocimientos varchar(70) NOT NULL, manejoEquipo varchar(70) NOT NULL, reqFisicos varchar(70) NOT NULL, reqPsicologicos varchar(70) NOT NULL, responsabilidades varchar(70) NOT NULL, condicionesTrabajo varchar(70) NOT NULL, PRIMARY KEY (idPuesto), KEY idEscolaridad (idEscolaridad), KEY idEstadoCivil (idEstadoCivil), KEY idGradoAvance (idGradoAvance), KEY idCarrera (idCarrera), KEY area (idArea))")
            self.cursor.execute("SELECT COUNT(*) FROM puesto")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO puesto (codPuesto, idArea, nomPuesto, puestoJefeSup, jornada, remunMensual, prestaciones, descripcionGeneral, funciones, edad, sexo, idEstadoCivil, idEscolaridad, idGradoAvance, idCarrera, experiencia, conocimientos, manejoEquipo, reqFisicos, reqPsicologicos, responsabilidades, condicionesTrabajo) VALUES ('V009', 5, 'SUPERVISOR DE TIENDA ', 'SUPERVISOR', 'LUNES A VIERNES', 5000, 'DE LEY', 'SUPERVISAR LAS ENTRADAS Y SALIDAS DE LA TIENDA', 'SUPERVISAR', '18 A 45 AÑOS', 'Hombre', 1, 3, 2, 2, '2 AÑOS', 'PROTECCION', 'MAQUINARIA Y COMUNICADORES', 'AGUDEZA VISUAL', 'MEMORIA A CORTO Y LARGO PLAZO', 'SEGURIDAD DE LA TIENDA', 'AGRADABLES')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO puesto (codPuesto, idArea, nomPuesto, puestoJefeSup, jornada, remunMensual, prestaciones, descripcionGeneral, funciones, edad, sexo, idEstadoCivil, idEscolaridad, idGradoAvance, idCarrera, experiencia, conocimientos, manejoEquipo, reqFisicos, reqPsicologicos, responsabilidades, condicionesTrabajo) VALUES ('v0008', 3, 'OFICIAL DE SEGURIDAD', 'SUPERVISOR', 'LUNES A VIERNES', 5000, 'DE LEY', 'CUIDAR Y PROTEGER ZONAS', 'CUIDAR Y VIGILAR', '18 A 45 AÑOS', 'Indistinto', 1, 2, 2, 1, '2 AÑOS', 'PROTECCION Y DEFENSA', 'MAQUINARIA Y ARMAS BLANCAS', 'AGUDEZA VISUAL', 'MEMORIA A CORTO Y LARGO PLAZO', 'SEGURIDAD DE PERSONAL', 'AGRADABLES')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO puesto (codPuesto, idArea, nomPuesto, puestoJefeSup, jornada, remunMensual, prestaciones, descripcionGeneral, funciones, edad, sexo, idEstadoCivil, idEscolaridad, idGradoAvance, idCarrera, experiencia, conocimientos, manejoEquipo, reqFisicos, reqPsicologicos, responsabilidades, condicionesTrabajo) VALUES ('p001', 5, 'COORDINADOR DE SEGURIDAD', 'GERENTE', 'LUNES A VIERNES 8:30am 4:30am SABADOS 9:00am  A 2:00am', 6500, 'DE LEY', 'COORDINAR A PERSONAL DE SEGURIDAD', 'COORDINACIÓN', '25 A 50', 'Indistinto', 1, 3, 4, 13, '2 AÑOS', 'TRATAR Y GUIAR A PERSONAL', 'COMUNICADORES Y ELECTRONICOS', 'NO NECESARIOS', 'MEMORIA A CORTO Y LARGO PLAZO', 'NO ESPECIFICADAS', 'AGRADABLES')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla puesto: {0}".format(err))

    def crearTablaPuestoHab(self):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS `puesto_has_habilidad` (  `idPuesto` int(11) NOT NULL,  `idEmpleado` int(11) NOT NULL,  `idHabilidad` int(11) NOT NULL,  PRIMARY KEY (`idPuesto`, `idEmpleado`,`idHabilidad`),  KEY `idHabilidad` (`idHabilidad`)) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;")
            self.cursor.execute("SELECT COUNT(*) FROM puesto_has_habilidad")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO `puesto_has_habilidad` (`idPuesto`,  `idEmpleado`, `idHabilidad`) VALUES(1,1, 1),(3,3, 4),(3,3, 5),(5,3, 2),(5,5, 3),(5,5, 4),(5,5, 5),(5,5, 6),(5,5, 7),(5,5, 8),(5,5, 9),(5,5, 10),(5,5, 11),(5,5, 12);")
                
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla puesto_has_habilidad: {0}".format(err))

    def crearTablaPuestoIdi(self):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS `puesto_has_idioma` (`idPuesto` int(11) NOT NULL,`idEmpleado` int(11) NOT NULL,`idIdioma` int(11) NOT NULL,PRIMARY KEY (`idPuesto`, `idEmpleado`,`idIdioma`),KEY `idIdioma` (`idIdioma`)) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;")
            self.cursor.execute("SELECT COUNT(*) FROM puesto_has_idioma")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO `puesto_has_idioma` (`idPuesto`,`idEmpleado`, `idIdioma`) VALUES(1, 1, 2),(3, 3, 1),(5, 5, 2);")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla puesto_has_idioma: {0}".format(err))

    def crearTablaRequisicion(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists requisicion (idRequisicion int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, folio varchar(25) NOT NULL, fechaElab date NOT NULL, fechaRecluta date NOT NULL, fechaInicVac date NOT NULL, motivoRequisicion varchar(30) NOT NULL, motivoEspecifique varchar(70) NOT NULL, tipoVacante varchar(15) NOT NULL, nomSolicita varchar(70) NOT NULL, nomAutoriza varchar(70) NOT NULL, nomRevisa varchar(70) NOT NULL, autorizada tinyint(1) NOT NULL, idPuesto int(11) NOT NULL, idArea int(11) NOT NULL, KEY idPuesto (idPuesto), KEY idArea (idArea))")
            self.cursor.execute("SELECT COUNT(*) FROM requisicion")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO requisicion (folio, fechaElab, fechaRecluta, fechaInicVac, motivoRequisicion, motivoEspecifique, tipoVacante, nomSolicita, nomAutoriza, nomRevisa, autorizada, idPuesto, idArea) VALUES ('1', '0000-00-00', '0000-00-00', '0000-00-00', 'BAJA', '', 'PERMANENTE', 'LUIS', 'LUIS, JEFE DE SEGURIDAD', 'JUAN', 1, 1, 1)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO requisicion (folio, fechaElab, fechaRecluta, fechaInicVac, motivoRequisicion, motivoEspecifique, tipoVacante, nomSolicita, nomAutoriza, nomRevisa, autorizada, idPuesto, idArea) VALUES ('2', '2023-11-23', '2023-11-27', '2023-12-01', 'OTRO', 'TEMPORADA', 'TEMPORAL', 'LUIS', 'LUIS, JEFE DE PROTECCION', 'JOSE', 1, 2, 1)")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla requisicion: {0}".format(err))

    def crearTablaUsuario(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists usuario (idusuario int(11) not null auto_increment PRIMARY KEY, numero int(10) not null unique, nombre varchar(120) not null, telefono int(13) not null, direccion varchar(100) not null, curp varchar(18) not null, vacante varchar(50) not null)")
            self.cursor.execute("SELECT COUNT(*) FROM usuario")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO usuario (numero, nombre, telefono, direccion, curp, vacante) VALUES (123238445,'Juan del montes',4493454564,'calle noche buena 120','kjfdhg495kg','Obrero')")
                self.conn.commit()
                self.conn.commit()
                self.cursor.execute("INSERT INTO usuario (numero, nombre, telefono, direccion, curp, vacante) VALUES (456456445,'Juan de los montes',4493454584,'calle noche buena 122','kjfdhg495kg','Marquetink')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO usuario (numero, nombre, telefono, direccion, curp, vacante) VALUES (123232498,'Juan del rancho',4493659564,'calle noche buena 123','kjfdhg495kg','Panista')")
                self.conn.commit()
                self.cursor.execute("INSERT INTO usuario (numero, nombre, telefono, direccion, curp, vacante) VALUES (123232425,'Juan del terreno',4493454964,'calle noche buena 124','kjfdhg495kg','Contador')")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla usuario: {0}".format(err))

    def crearTablaVacante(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists vacante (idVacante int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, conseVR int(11) NOT NULL, fuenteCandidato varchar(40) NOT NULL, inicioFechaPublic date NOT NULL, finFechaPublic date NOT NULL, publicada tinyint(4) NOT NULL, observaciones varchar(40) NOT NULL, candidatoSelecc int(11) NOT NULL, fechaContratacion date NOT NULL, idRequisicion int(11) NOT NULL, idPuesto int(11) NOT NULL)")
            self.cursor.execute("SELECT COUNT(*) FROM vacante")
            count = self.cursor.fetchone()[0]
            if count == 0:
                self.cursor.execute("INSERT INTO vacante (conseVR, fuenteCandidato, inicioFechaPublic, finFechaPublic, publicada, observaciones, candidatoSelecc, fechaContratacion, idRequisicion, idPuesto) VALUES (0, 'Interno', '2023-11-23', '2023-11-27', 1, 'VACANTE PARA CONTRATAR PERSONAL', 0, '2023-12-12', 1, 1)")
                self.conn.commit()
                self.cursor.execute("INSERT INTO vacante (conseVR, fuenteCandidato, inicioFechaPublic, finFechaPublic, publicada, observaciones, candidatoSelecc, fechaContratacion, idRequisicion, idPuesto) VALUES (0, 'Externo', '2023-09-13', '2023-12-27', 1, 'VACANTE PARA REEMPLAZAR PERSONAL', 0, '2024-01-25', 2, 2)")
                self.conn.commit()
        except pymysql.Error as err:
            print("\nError al crear la tabla vacante: {0}".format(err))

# Cerramos la base de datos junto con el cursor
    def closeDB(self):
        self.cursor.close()
        self.conection.close()

# Conectamos a la bd y llamamos a las funciones para crear las tablas, y mostrar error en caso de que exista
    def conectar(self):
        try:
            self.crearTablaAgcuso()
            self.crearTablaArea()
            self.crearTablaCalificaciones()
            self.crearTablaCandidato()
            self.crearTablaCarrera()
            self.crearTablaCompletadas()
            self.crearTablaCursos()
            self.crearTablaDoctoSolic()
            self.crearTablaEmpleado()
            self.crearTablaEscolaridad()
            self.crearTablaEstadoCivil()
            self.crearTablaExamen()
            self.crearTablaGradoA()
            self.crearTablaHabilidad()
            self.crearTablaIdioma()
            self.crearTablaMedioPub()
            self.crearTablaPuesto()
            self.crearTablaPuestoHab()
            self.crearTablaPuestoIdi()
            self.crearTablaRequisicion()
            self.crearTablaUsuario()
            self.crearTablaVacante()
            

        except pymysql.Error as err: 
            print ("\nError al intentar la conexión: {0}".format(err))

