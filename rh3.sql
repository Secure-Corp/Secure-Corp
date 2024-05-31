-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-05-2024 a las 17:23:31
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rh3`
--
CREATE DATABASE IF NOT EXISTS `rh3` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `rh3`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `area`
--

CREATE TABLE IF NOT EXISTS `area` (
  `idArea` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(60) NOT NULL,
  PRIMARY KEY (`idArea`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `area`
--

INSERT INTO `area` (`idArea`, `descripcion`) VALUES
(1, 'DIRECCION GENERAL'),
(2, 'ADMINISTRACION Y RECURSOS HUMANOS'),
(3, 'PRODUCCION'),
(4, 'FINANZAS Y CONTABILIDAD'),
(5, 'MERCADOTECNIA'),
(6, 'INFORMATICA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `candidato`
--

CREATE TABLE IF NOT EXISTS `candidato` (
  `idCandidato` int(11) NOT NULL AUTO_INCREMENT,
  `idVacante` int(11) NOT NULL,
  `idRequisicion` int(11) NOT NULL,
  `idPuesto` int(11) NOT NULL,
  `CURP` varchar(30) NOT NULL,
  `RFC` varchar(20) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `domCalle` varchar(40) NOT NULL,
  `domNumExtInt` varchar(30) NOT NULL,
  `domColonia` varchar(40) NOT NULL,
  `tel1` varchar(20) NOT NULL,
  `tel2` varchar(20) NOT NULL,
  `correoE` varchar(40) NOT NULL,
  `edad` int(11) NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `idEstadoCivil` int(11) NOT NULL,
  `idEscolaridad` int(11) NOT NULL,
  `idGradoAvance` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  `entrevSelecReq` tinyint(4) NOT NULL,
  `entrevSelecPresen` tinyint(4) NOT NULL,
  `entrevSelecResult` varchar(40) NOT NULL,
  `evalMedicaReq` tinyint(4) NOT NULL,
  `evalMedicaPresen` tinyint(4) NOT NULL,
  `evalMedicaResult` varchar(40) NOT NULL,
  `evalPsicolgReq` tinyint(4) NOT NULL,
  `evalPsicologPresen` tinyint(4) NOT NULL,
  `evalPsicologResult` varchar(40) NOT NULL,
  `evalPsicometReq` tinyint(4) NOT NULL,
  `evalPsicometPresene` tinyint(4) NOT NULL,
  `evalPsicometResult` varchar(40) NOT NULL,
  `evalTecnicaReq` tinyint(4) NOT NULL,
  `evalTecnicaPresen` tinyint(4) NOT NULL,
  `evalTecnicaResult` varchar(41) NOT NULL,
  `evalConocReq` tinyint(4) NOT NULL,
  `evalConocPresen` tinyint(4) NOT NULL,
  `evalConocResult` varchar(40) NOT NULL,
  `entrevFinalReq` tinyint(4) NOT NULL,
  `entrevFinalPresen` tinyint(4) NOT NULL,
  `entrevFinalResul` varchar(40) NOT NULL,
  PRIMARY KEY (`idCandidato`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `candidato`
--

INSERT INTO `candidato` (`idCandidato`, `idVacante`, `idRequisicion`, `idPuesto`, `CURP`, `RFC`, `nombre`, `domCalle`, `domNumExtInt`, `domColonia`, `tel1`, `tel2`, `correoE`, `edad`, `sexo`, `idEstadoCivil`, `idEscolaridad`, `idGradoAvance`, `idCarrera`, `entrevSelecReq`, `entrevSelecPresen`, `entrevSelecResult`, `evalMedicaReq`, `evalMedicaPresen`, `evalMedicaResult`, `evalPsicolgReq`, `evalPsicologPresen`, `evalPsicologResult`, `evalPsicometReq`, `evalPsicometPresene`, `evalPsicometResult`, `evalTecnicaReq`, `evalTecnicaPresen`, `evalTecnicaResult`, `evalConocReq`, `evalConocPresen`, `evalConocResult`, `entrevFinalReq`, `entrevFinalPresen`, `entrevFinalResul`) VALUES
(1, 1, 1, 1, 'ROGH760106MASDML03', 'dfadf', 'fasdfads', 'adsfa', '23', 'erqwr', '32', '23', 'rqwr', 23, 'Indistinto', 1, 2, 1, 1, 0, 0, '', 0, 0, '', 0, 0, '', 0, 0, '', 0, 0, '', 0, 0, '', 0, 0, ''),
(2, 1, 1, 1, 'ROML551119HASDCR08', 'dfadf', 'juan', 'adsfa', '23', 'erqwr', '32', '23', 'rqwr', 23, 'Indistinto', 3, 2, 3, 1, 0, 0, '', 0, 0, '', 0, 0, '', 0, 0, '', 0, 0, '', 0, 0, '', 0, 0, '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrera`
--

CREATE TABLE IF NOT EXISTS `carrera` (
  `idCarrera` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL,
  PRIMARY KEY (`idCarrera`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `carrera`
--

INSERT INTO `carrera` (`idCarrera`, `descripcion`) VALUES
(1, 'NO APLICA'),
(2, 'ADMINISTRACION DE EMPRESAS'),
(3, 'ADMINISTRACIÓN DE PRODUCCIÓN Y SERVICIOS'),
(4, 'ADMINISTRACIÓN FINANCIERA'),
(5, 'COMERCIO INTERNACIONAL'),
(6, 'COMERCIO ELECTRONICO'),
(7, 'COMUNICACION'),
(8, 'CONTADOR '),
(9, 'DERECHO'),
(10, 'ECONOMIA'),
(11, 'GESTION TURISTICA'),
(12, 'LOGISTICA EMPRESARIAL'),
(13, 'MERCADOTECNIA'),
(14, 'SISTEMAS COMPUTACIONALES Y AFINES'),
(15, 'INDUSTRIAL'),
(16, 'ELECTRICA'),
(17, 'ROBOTICA'),
(18, 'RELACIONES INDUSTRIALES'),
(19, 'PSICOLOGIA'),
(20, 'ELECTRONICA'),
(21, 'GESTION EMPRESARIAL');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `docto_solic`
--

CREATE TABLE IF NOT EXISTS `docto_solic` (
  `idDoctoSolic` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(70) NOT NULL,
  `original` varchar(2) NOT NULL,
  `numCopias` int(5) NOT NULL,
  PRIMARY KEY (`idDoctoSolic`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `docto_solic`
--

INSERT INTO `docto_solic` (`idDoctoSolic`, `descripcion`, `original`, `numCopias`) VALUES
(1, 'Solicitud de empleo', 'SI', 1),
(2, 'CURRICULUM VITAE con fotografía', 'SI', 1),
(3, 'Carta de presentación', 'SI', 1),
(4, 'Carta de recomendación', 'SI', 1),
(5, 'Comprobante de domicilio reciente', 'NO', 2),
(6, 'Acta de nacimiento', 'SI', 1),
(7, 'Número del seguro social', 'NO', 2),
(8, 'CURP', 'NO', 2),
(9, 'Credencial para votar', 'NO', 2),
(10, 'Licencia automovilista', 'NO', 2),
(11, 'Licencia chofer', 'NO', 2),
(12, 'Certificado Carrera Comercial o Técnica', 'NO', 2),
(13, 'Certificado Preparatoria o Equivalente', 'NO', 2),
(14, 'Certificado Licenciatura o Equivalente', 'NO', 2),
(15, 'Constancia de Estudios', 'SI', 2),
(16, 'Carta de Pasante Carrera Técnica', 'NO', 2),
(17, 'Carta de Pasante Licenciatura', 'NO', 2),
(18, 'Carta de Pasante Posgrado', 'NO', 2),
(19, 'Cédula Profesional', 'NO', 2),
(20, 'Título Licenciatura', 'NO', 2),
(21, 'Título Posgrado', 'NO', 2),
(22, 'Certificado Médico', 'SI', 2),
(23, 'Antecedentes No penales', 'Si', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escolaridad`
--

CREATE TABLE IF NOT EXISTS `escolaridad` (
  `idEscolaridad` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL,
  PRIMARY KEY (`idEscolaridad`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `escolaridad`
--

INSERT INTO `escolaridad` (`idEscolaridad`, `descripcion`) VALUES
(1, 'NO APLICA / NO REQUERIDA '),
(2, 'PREPARATORIA'),
(3, 'CARRERA TÉCNICA O COMERCIAL'),
(4, 'BACHILLERATO TÉCNICO O ESPECIALIZADO'),
(5, 'TÉCNICO SUPERIOR UNIVERSITARIO'),
(6, 'LICENCIATURA / INGENIERÍA / PROFESIONAL'),
(7, 'MAESTRIA'),
(8, 'DOCTORADO'),
(9, 'KINDER');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_civil`
--

CREATE TABLE IF NOT EXISTS `estado_civil` (
  `idEstadoCivil` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL,
  PRIMARY KEY (`idEstadoCivil`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `estado_civil`
--

INSERT INTO `estado_civil` (`idEstadoCivil`, `descripcion`) VALUES
(1, 'INDISTINTO'),
(2, 'SOLTERO'),
(3, 'CASADO'),
(4, 'UNION LIBRE');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grado_avance`
--

CREATE TABLE IF NOT EXISTS `grado_avance` (
  `idGradoAvance` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(45) NOT NULL,
  PRIMARY KEY (`idGradoAvance`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `grado_avance`
--

INSERT INTO `grado_avance` (`idGradoAvance`, `descripcion`) VALUES
(1, 'NO APLICA'),
(2, 'CURSANDO'),
(3, 'TERMINADO'),
(4, 'INCONCLUSO'),
(5, 'PASANTE'),
(6, 'TITULADO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habilidad`
--

CREATE TABLE IF NOT EXISTS `habilidad` (
  `idHabilidad` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(150) NOT NULL,
  PRIMARY KEY (`idHabilidad`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `habilidad`
--

INSERT INTO `habilidad` (`idHabilidad`, `descripcion`) VALUES
(1, 'NO REQUERIDAS'),
(2, 'FACILIDAD DE PALABRA'),
(3, 'MANEJO DE CONFLICTOS'),
(4, 'CAPACIDAD PARA TRABAJAR BAJO PRESION'),
(5, 'CAPACIDAD DE TRABAJO EN EQUIPO'),
(6, 'TOMA DE DECISIONES'),
(7, 'PENSAMIENTO CREATIVO'),
(8, 'PENSAMIENTO CRITICO'),
(9, 'MANEJO DE EMOCIONES'),
(10, 'PROACTIVIDAD'),
(11, 'PROFESIONALIDAD'),
(12, 'ESCUCHA ACTIVA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `idioma`
--

CREATE TABLE IF NOT EXISTS `idioma` (
  `idIdioma` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL,
  PRIMARY KEY (`idIdioma`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `idioma`
--

INSERT INTO `idioma` (`idIdioma`, `descripcion`) VALUES
(1, 'NO REQUERIDO'),
(2, 'INGLES BASICO'),
(3, 'INGLES INTERMEDIO'),
(4, 'INGLES AVANZADO'),
(5, 'JAPONES BASICO'),
(6, 'JAPONES CONVERSACIONAL'),
(7, 'JAPONES ESCRITO Y CONVERSACIONAL'),
(9, 'ALEMAN AVANZADO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mediopublic`
--

CREATE TABLE IF NOT EXISTS `mediopublic` (
  `idMedioPublic` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(70) NOT NULL,
  PRIMARY KEY (`idMedioPublic`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `mediopublic`
--

INSERT INTO `mediopublic` (`idMedioPublic`, `descripcion`) VALUES
(1, 'Convocatoria en áreas estratégicas de la empresa'),
(2, 'Sitio web de la empresa'),
(3, 'Servicio estatal de empleo'),
(4, 'Redes sociales para empleo'),
(5, 'Agencia particular de empleo'),
(6, 'Radio'),
(7, 'Televisión'),
(8, 'Periódico Digital');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto`
--

CREATE TABLE IF NOT EXISTS `puesto` (
  `idPuesto` int(11) NOT NULL AUTO_INCREMENT,
  `codPuesto` varchar(15) NOT NULL,
  `idArea` int(11) NOT NULL,
  `nomPuesto` varchar(50) NOT NULL,
  `puestoJefeSup` varchar(50) NOT NULL,
  `jornada` varchar(70) NOT NULL,
  `remunMensual` int(11) NOT NULL,
  `prestaciones` varchar(70) NOT NULL,
  `descripcionGeneral` varchar(250) NOT NULL,
  `funciones` varchar(250) NOT NULL,
  `edad` varchar(50) NOT NULL,
  `sexo` varchar(15) NOT NULL,
  `idEstadoCivil` int(11) NOT NULL,
  `idEscolaridad` int(11) NOT NULL,
  `idGradoAvance` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  `experiencia` varchar(70) NOT NULL,
  `conocimientos` varchar(70) NOT NULL,
  `manejoEquipo` varchar(70) NOT NULL,
  `reqFisicos` varchar(70) NOT NULL,
  `reqPsicologicos` varchar(70) NOT NULL,
  `responsabilidades` varchar(70) NOT NULL,
  `condicionesTrabajo` varchar(70) NOT NULL,
  PRIMARY KEY (`idPuesto`),
  KEY `idEscolaridad` (`idEscolaridad`),
  KEY `idEstadoCivil` (`idEstadoCivil`),
  KEY `idGradoAvance` (`idGradoAvance`),
  KEY `idCarrera` (`idCarrera`),
  KEY `area` (`idArea`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `puesto`
--

INSERT INTO `puesto` (`idPuesto`, `codPuesto`, `idArea`, `nomPuesto`, `puestoJefeSup`, `jornada`, `remunMensual`, `prestaciones`, `descripcionGeneral`, `funciones`, `edad`, `sexo`, `idEstadoCivil`, `idEscolaridad`, `idGradoAvance`, `idCarrera`, `experiencia`, `conocimientos`, `manejoEquipo`, `reqFisicos`, `reqPsicologicos`, `responsabilidades`, `condicionesTrabajo`) VALUES
(1, 'V009', 5, 'SUPERVISOR DE TIENDA ', 'SUPERVISOR', 'LUNES A VIERNES', 5000, 'DE LEY', 'VENTAS AL PÚBLICO', 'VENDER', '18 A 45 AÑOS', 'Hombre', 1, 3, 2, 2, '2 AÑOS', 'VENTAS', 'DE COMPUTO', 'AGUDEZA VISUAL', 'MEMORIA A CORTO Y LARGO PLAZO', 'INVENTARIO', 'AGRADABLES'),
(3, 'v0008', 3, 'OBRERO', 'SUPERVISOR', 'LUNES A VIERNES', 5000, 'DE LEY', 'maquilar', 'trabajar', '18 A 45 AÑOS', 'Indistinto', 1, 2, 2, 1, '2 AÑOS', 'VENTAS', 'DE COMPUTO', 'AGUDEZA VISUAL', 'MEMORIA A CORTO Y LARGO PLAZO', 'INVENTARIO', 'AGRADABLES'),
(5, 'p001', 5, 'JEFE DE MERCADOTECNIA', 'GERENTE', 'LUNES A VIERNES 8:30am 4:30am SABADOS 9:00am  A 2:00am', 6500, 'DE LEY', 'COORDINAR A PERSONAL DE MERCADOTECNIA', 'CORDINACIÓN', '25 A 50', 'Indistinto', 1, 3, 4, 13, '2 AÑOS', 'VENTAS', 'DE COMPUTO', 'NO NECESARIOS', 'MEMORIA A CORTO Y LARGO PLAZO', 'NO ESPECIFICADAS', 'AGRADABLES');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto_has_habilidad`
--

CREATE TABLE IF NOT EXISTS `puesto_has_habilidad` (
  `idPuesto` int(11) NOT NULL,
  `idHabilidad` int(11) NOT NULL,
  PRIMARY KEY (`idPuesto`,`idHabilidad`),
  KEY `idHabilidad` (`idHabilidad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `puesto_has_habilidad`
--

INSERT INTO `puesto_has_habilidad` (`idPuesto`, `idHabilidad`) VALUES
(1, 1),
(3, 4),
(3, 5),
(5, 2),
(5, 3),
(5, 4),
(5, 5),
(5, 6),
(5, 7),
(5, 8),
(5, 9),
(5, 10),
(5, 11),
(5, 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto_has_idioma`
--

CREATE TABLE IF NOT EXISTS `puesto_has_idioma` (
  `idPuesto` int(11) NOT NULL,
  `idIdioma` int(11) NOT NULL,
  PRIMARY KEY (`idPuesto`,`idIdioma`),
  KEY `idIdioma` (`idIdioma`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `puesto_has_idioma`
--

INSERT INTO `puesto_has_idioma` (`idPuesto`, `idIdioma`) VALUES
(1, 2),
(3, 1),
(5, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `requisicion`
--

CREATE TABLE IF NOT EXISTS `requisicion` (
  `idRequisicion` int(11) NOT NULL AUTO_INCREMENT,
  `folio` varchar(25) NOT NULL,
  `fechaElab` date NOT NULL,
  `fechaRecluta` date NOT NULL,
  `fechaInicVac` date NOT NULL,
  `motivoRequisicion` varchar(30) NOT NULL,
  `motivoEspecifique` varchar(70) NOT NULL,
  `tipoVacante` varchar(15) NOT NULL,
  `nomSolicita` varchar(70) NOT NULL,
  `nomAutoriza` varchar(70) NOT NULL,
  `nomRevisa` varchar(70) NOT NULL,
  `autorizada` tinyint(1) NOT NULL,
  `idPuesto` int(11) NOT NULL,
  `idArea` int(11) NOT NULL,
  PRIMARY KEY (`idRequisicion`),
  KEY `idPuesto` (`idPuesto`),
  KEY `idArea` (`idArea`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `requisicion`
--

INSERT INTO `requisicion` (`idRequisicion`, `folio`, `fechaElab`, `fechaRecluta`, `fechaInicVac`, `motivoRequisicion`, `motivoEspecifique`, `tipoVacante`, `nomSolicita`, `nomAutoriza`, `nomRevisa`, `autorizada`, `idPuesto`, `idArea`) VALUES
(1, '1', '0000-00-00', '0000-00-00', '0000-00-00', '1', '', '', 'LUIS, JEFE DE VENTAS', 'luis', 'juan', 1, 1, 1),
(10, '2', '2023-11-23', '2023-11-27', '2023-12-01', 'Otro', 'temporada', 'Temporal', 'LUIS, JEFE DE VENTAS', 'luis', 'juan', 1, 1, 1);


CREATE TABLE IF NOT EXISTS `examen` (
  `idExamen` int(11) NOT NULL AUTO_INCREMENT, 
  `nombre` varchar(70) NOT NULL,
  `rfc` varchar(20)NOT NULL,
  `preg1` varchar(250) NOT NULL,
  `preg2` varchar(250) NOT NULL,
  `preg3` varchar(250) NOT NULL,
  `preg4` varchar(250) NOT NULL,
  `preg5` varchar(250) NOT NULL,
  `preg6` varchar(250) NOT NULL,
  `preg7` varchar(250) NOT NULL,
  `preg8` varchar(250) NOT NULL,
  `preg9` varchar(250) NOT NULL,
  `preg10` varchar(250) NOT NULL,
  `preg11` varchar(250) NOT NULL,
  `preg12` varchar(250) NOT NULL,
  PRIMARY KEY (`idExamen`)
);

CREATE TABLE IF NOT EXISTS `calificaciones` (
  `idCalificacion` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `rfc` varchar(20)NOT NULL,
  `calificacion` int(11) NOT NULL,
  `preg1` varchar(250) NOT NULL,
  `preg2` varchar(250) NOT NULL,
  `preg3` varchar(250) NOT NULL,
  `preg4` varchar(250) NOT NULL,
  `preg5` varchar(250) NOT NULL,
  `preg6` varchar(250) NOT NULL,
  `preg7` varchar(250) NOT NULL,
  `preg8` varchar(250) NOT NULL,
  `preg9` varchar(250) NOT NULL,
  `preg10` varchar(250) NOT NULL,
  `preg11` varchar(250) NOT NULL,
  `preg12` varchar(250) NOT NULL,
  PRIMARY KEY (`idCalificacion`)
);



-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vacante`
--

CREATE TABLE IF NOT EXISTS `vacante` (
  `idVacante` int(11) NOT NULL AUTO_INCREMENT,
  `conseVR` int(11) NOT NULL,
  `fuenteCandidato` varchar(40) NOT NULL,
  `inicioFechaPublic` date NOT NULL,
  `finFechaPublic` date NOT NULL,
  `publicada` tinyint(4) NOT NULL,
  `observaciones` varchar(40) NOT NULL,
  `candidatoSelecc` int(11) NOT NULL,
  `fechaContratacion` date NOT NULL,
  `idRequisicion` int(11) NOT NULL,
  `idPuesto` int(11) NOT NULL,
  PRIMARY KEY (`idVacante`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `vacante`
--

INSERT INTO `vacante` (`idVacante`, `conseVR`, `fuenteCandidato`, `inicioFechaPublic`, `finFechaPublic`, `publicada`, `observaciones`, `candidatoSelecc`, `fechaContratacion`, `idRequisicion`, `idPuesto`) VALUES
(1, 0, 'Interno', '2023-11-23', '2023-11-27', 1, 'gfgf', 0, '0000-00-00', 1, 1);
COMMIT;


-- Empleados

CREATE TABLE `empleado` (
  `idEmpleado` int(11) NOT NULL AUTO_INCREMENT,
  `idRequisicion` int(11) NOT NULL,
  `idPuesto` int(11) NOT NULL,
  `CURP` varchar(30) NOT NULL,
  `RFC` varchar(20) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `apellido` varchar(40) NOT NULL,
  `domCalle` varchar(40) NOT NULL,
  `domNumExtInt` varchar(30) NOT NULL,
  `domColonia` varchar(40) NOT NULL,
  `tel1` varchar(20) NOT NULL,
  `sueldo` varchar(20) NOT NULL,
  `correoE` varchar(40) NOT NULL,
  `edad` int(11) NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `idEstadoCivil` int(11) NOT NULL,
  `idEscolaridad` int(11) NOT NULL,
  `idGradoAvance` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  PRIMARY KEY (`idEmpleado`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;


--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleado` (`idEmpleado`, `idRequisicion`, `idPuesto`, `CURP`, `RFC`, `nombre`, `apellido`, `domCalle`, `domNumExtInt`, `domColonia`, `tel1`, `sueldo`, `correoE`, `edad`, `sexo`, `idEstadoCivil`, `idEscolaridad`, `idGradoAvance`, `idCarrera`) VALUES
(1, 1, 1, 'ROGH760106MASDML03', 'dfadf', 'Carlitos', 'Muntez', 'Villas', '#23', 'palmas', '4491102343', '$233', 'carlitos@gmail.com', 23, 'Macho', 1, 2, 1, 1),
(2, 1, 1, 'ROML551119HASDCR08', 'dfajy', 'Pepe', 'Maciado', 'Potreros', '#26', 'cruz', '4491739435', '$2223', 'pepe@gmail.com', 23, 'Indistinto', 3, 2, 3, 1);


 
 -- 
 -- Encuentra la tabal de la tabla "cursos"
 --
 create table IF not exists `cursos`(
 `idcursos` int(11) not null auto_increment,
 `nombre` varchar(50) not null,
 `descripcion` varchar(120) not null,
 `Video` varchar(1000) not null,
 `nombren` varchar(120) not null,
 `Informacion` varchar(2000) not null,
 primary key(`idcursos`)
 );
 
--
-- Volcado de datos para la tabla `cursos`
--
 
--
-- estructura de la tabla para agregar cursos a un usuario
--
  create table IF not exists `agcuso`(
 `idagcu` int(11) not null auto_increment,
 `nombre` varchar(50) not null,
 `descripcion` varchar(120) not null,
 `completado` int(3) not null,
 `idusuario` int(11) not null,
 primary key(`idagcu`)
 );

--
-- estructura para marcar el estado de un  curso
--
create table IF not exists `completadas`(
 `id` int(11) not null auto_increment,
 `descripcion` varchar(2) not null,
 primary key(`id`)
 );
 --
-- tabla de apoyo para el estado de un curso
--
 insert into `completadas`(`descripcion`) VALUES 
 ('si'),
('no');
