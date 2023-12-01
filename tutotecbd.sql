-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-12-2023 a las 01:35:23
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tutotecbd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `no_control` varchar(30) NOT NULL COMMENT 'Número de control del estudiante.',
  `nombre` varchar(45) NOT NULL COMMENT 'Nombre del usuario (alumno).',
  `apellido_pa` varchar(45) NOT NULL COMMENT 'Apellido paterno del usuario.',
  `apellido_ma` varchar(45) NOT NULL COMMENT 'Apellido materno del usuario.',
  `carrera` varchar(100) NOT NULL COMMENT 'Carrera a la que pertenece el alumno',
  `grupo` varchar(30) NOT NULL COMMENT 'Grupo al que pertenece el usuario.',
  `correo` varchar(100) NOT NULL COMMENT 'Correo institucional del alumno',
  `password` varchar(30) NOT NULL COMMENT 'Contraseña la cual puede incluir números y letras.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `alumnos`
--

INSERT INTO `alumnos` (`no_control`, `nombre`, `apellido_pa`, `apellido_ma`, `carrera`, `grupo`, `correo`, `password`) VALUES
('S20030134', 'Alinne Samantha', 'Hernández', 'Pérez', 'Sistemas', '077CA', 'admin@gmail.com', '123456'),
('S20030135', 'Faker', 'Lee', 'Sang-Hyeok', 'INGENIERÍA EN SISTEMAS COMPUTA', '077CA', 'faker@elmejor.com', 'faker'),
('s20030136', 'hola', 'pap', 'mam', 'siuu', '077ca', 'hola@admin.com', '123456');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitudes`
--

CREATE TABLE `solicitudes` (
  `id` int(15) NOT NULL COMMENT 'Id de la solicitud.',
  `nombre` varchar(45) NOT NULL COMMENT 'Nombre del usuario que realiza la solicitud.',
  `apellido_pa` varchar(45) NOT NULL COMMENT 'Apellido paterno del usuario.',
  `apellido_ma` varchar(45) NOT NULL COMMENT 'Apellido materno del usuario.',
  `tema_solicitado` varchar(45) NOT NULL COMMENT 'Tema del que trata la solicitud.',
  `fecha` date NOT NULL COMMENT 'Fecha en la que se realiza la solicitud.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tutores`
--

CREATE TABLE `tutores` (
  `correo` varchar(45) NOT NULL COMMENT 'Correo del usuario (tutor) con el que iniciará sesión.',
  `nombre` varchar(45) NOT NULL COMMENT 'Nombre del usuario.',
  `apellido_pa` varchar(45) NOT NULL COMMENT 'Apellido paterno del usuario.',
  `apellido_ma` varchar(45) NOT NULL COMMENT 'Apellido materno del usuario.',
  `academia` varchar(30) NOT NULL COMMENT 'Nombre de la academia a la que pertenece el usuario.',
  `grupo` varchar(30) NOT NULL COMMENT 'Grupo al que se encuentra asignado el usuario para impartir las tutorías.',
  `password` varchar(30) NOT NULL COMMENT 'Contraseña la cual puede incluir números y letras.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `tutores`
--

INSERT INTO `tutores` (`correo`, `nombre`, `apellido_pa`, `apellido_ma`, `academia`, `grupo`, `password`) VALUES
('admin@gmail.com', 'Juan Carlos', 'Madrigal', 'Hernandez', 'Sistemas', '077CA', '123'),
('hola@gmail.com', 'Cesar', 'mora', 'hernández', 'ingeniería en sistemas', '077ca', '123'),
('hola2@gmail.com', 'Esmeralda', 'delgado', 'perez', 'sistemas', '077ca', '456');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`no_control`);

--
-- Indices de la tabla `solicitudes`
--
ALTER TABLE `solicitudes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tutores`
--
ALTER TABLE `tutores`
  ADD PRIMARY KEY (`correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `solicitudes`
--
ALTER TABLE `solicitudes`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT COMMENT 'Id de la solicitud.';
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
