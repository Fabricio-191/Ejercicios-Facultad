-- SPRT2022

CREATE TYPE TIPO_VEHICULO AS ENUM ('Camion', 'Auto', 'Moto');
CREATE TYPE ORIENTACION AS ENUM ('N', 'S', 'E', 'O');

CREATE TABLE IF NOT EXISTS vehiculo (
    patente TEXT PRIMARY KEY,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    seguro TEXT NOT NULL,
    tipo TIPO_VEHICULO NOT NULL
	-- tipo TEXT NOT NULL CHECK(tipo IN ('Camion', 'Auto', 'Moto'))
);

CREATE TABLE IF NOT EXISTS camiones (
    patente TEXT PRIMARY KEY REFERENCES vehiculo(patente) ON DELETE CASCADE ON UPDATE CASCADE,
    valor INT NOT NULL CHECK (valor > 0),
    kilometraje INT NOT NULL CHECK (kilometraje > 0)
);

CREATE TABLE IF NOT EXISTS persona (
    cuil TEXT PRIMARY KEY,
    nombreyapellido TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS chofer (
    cuil TEXT PRIMARY KEY,
    antiguedad INT NOT NULL CHECK (antiguedad > 0),
    sueldo REAL NOT NULL CHECK (sueldo > 0)
);

CREATE TABLE IF NOT EXISTS choferes_camiones (
    cuil TEXT NOT NULL REFERENCES chofer(cuil) ON DELETE CASCADE ON UPDATE CASCADE,
    patente TEXT NOT NULL REFERENCES camiones(patente) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (cuil, patente)
);

CREATE TABLE IF NOT EXISTS provincia (
    nombre TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS localidad (
    codigo SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    provincia TEXT NOT NULL REFERENCES provincia(nombre) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS viaje (
    numero INT PRIMARY KEY,
    patenteCamion TEXT NOT NULL REFERENCES camiones(patente),
    cuilChofer TEXT NOT NULL REFERENCES chofer(cuil),
    kilometros REAL NOT NULL CHECK (kilometros > 0),
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL CHECK (fechaFin > fechaInicio)
);

CREATE TABLE IF NOT EXISTS viajeRecorrio (
    codigoLocalidad INT REFERENCES localidad(codigo),
    codigoViaje INT REFERENCES viaje(numero),
    PRIMARY KEY (codigoLocalidad, codigoViaje)
);

CREATE TABLE IF NOT EXISTS paquete (
    numero SERIAL PRIMARY KEY,
    numViaje INT NOT NULL REFERENCES viaje(numero) ON DELETE CASCADE ON UPDATE CASCADE,
    valor REAL NOT NULL CHECK (valor > 0),
    precioTranslado REAL NOT NULL CHECK (precioTranslado > 0),
    destinatarioCUIL TEXT NOT NULL,
    remitenteCUIL TEXT NOT NULL REFERENCES persona(cuil) ON DELETE CASCADE ON UPDATE CASCADE,
    entrega_localidad_codigo INT NOT NULL REFERENCES localidad(codigo) ON DELETE CASCADE ON UPDATE CASCADE,
    entrega_direccion_calle TEXT NOT NULL,
    entrega_direccion_orientacion ORIENTACION NOT NULL,
    entrega_direccion_numero INT NOT NULL
);

CREATE TABLE IF NOT EXISTS actaChoque (
    numero INT,
    provincia TEXT NOT NULL REFERENCES provincia(nombre) ON DELETE CASCADE ON UPDATE CASCADE,
    fecha DATE NOT NULL CHECK (fecha < CURRENT_DATE),
    costo REAL NOT NULL CHECK (costo > 0),
    descripcion TEXT NOT NULL,
	PRIMARY KEY (numero, provincia)
);

CREATE TABLE IF NOT EXISTS participoChoque (
    numeroChoque INT,
    provincia TEXT NOT NULL REFERENCES provincia(nombre) ON DELETE CASCADE ON UPDATE CASCADE,
    patenteVehiculo TEXT REFERENCES vehiculo(patente) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (numeroChoque, provincia, patenteVehiculo),
	FOREIGN KEY (numeroChoque, provincia) REFERENCES actaChoque(numero, provincia) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS viajeChoque (
    numeroChoque INT,
    provincia TEXT NOT NULL REFERENCES provincia(nombre) ON DELETE CASCADE ON UPDATE CASCADE,
    codigoViaje INT REFERENCES viaje(numero) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (numeroChoque, provincia, codigoViaje),
	FOREIGN KEY (numeroChoque, provincia) REFERENCES actaChoque(numero, provincia) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO provincia(nombre) VALUES
    ('Buenos Aires'),
    ('Ciudad Autónoma de Buenos Aires'),
    ('Catamarca'),
    ('Chaco'),
    ('Chubut'),
    ('Córdoba'),
    ('Corrientes'),
    ('Entre Ríos'),
    ('Formosa'),
    ('Jujuy'),
    ('La Pampa'),
    ('La Rioja'),
    ('Mendoza'),
    ('Misiones'),
    ('Neuquén'),
    ('Río Negro'),
    ('Salta'),
    ('San Juan'),
    ('San Luis'),
    ('Santa Cruz'),
    ('Santa Fe'),
    ('Santiago del Estero'),
    ('Tierra del Fuego, Antártida e Islas del Atlántico Sur'),
    ('Tucumán');

INSERT INTO localidad(nombre, provincia) VALUES
	('Localidad 1', 'Buenos Aires'),
	('Liniers', 'Buenos Aires'),
	('Localidad 3', 'Buenos Aires'),
	('Localidad 4', 'Ciudad Autónoma de Buenos Aires'),
	('Localidad 5', 'Ciudad Autónoma de Buenos Aires'),
	('Localidad 6', 'Ciudad Autónoma de Buenos Aires'),
	('Localidad 7', 'Catamarca'),
	('Localidad 8', 'Catamarca'),
	('Localidad 9', 'Catamarca'),
	('Localidad 10', 'Chaco'),
	('Localidad 11', 'Chaco'),
	('Localidad 12', 'Chaco'),
	('Localidad 13', 'Chubut'),
	('Localidad 14', 'Chubut'),
	('Localidad 15', 'Chubut'),
	('Localidad 16', 'Córdoba'),
	('Localidad 17', 'Córdoba'),
	('Localidad 18', 'Córdoba'),
	('Localidad 19', 'Corrientes'),
	('Localidad 20', 'Corrientes'),
	('Localidad 21', 'Corrientes'),
	('Localidad 22', 'Entre Ríos'),
	('Localidad 23', 'Entre Ríos'),
	('Localidad 24', 'Entre Ríos'),
	('Localidad 25', 'Formosa'),
	('Localidad 26', 'Formosa'),
	('Localidad 27', 'Formosa'),
	('Localidad 28', 'Jujuy'),
	('Localidad 29', 'Jujuy'),
	('Localidad 30', 'Jujuy'),
	('Localidad 31', 'La Pampa'),
	('Localidad 32', 'La Pampa'),
	('Localidad 33', 'La Pampa'),
	('Localidad 34', 'La Rioja'),
	('Localidad 35', 'La Rioja'),
	('Localidad 36', 'La Rioja'),
	('Localidad 37', 'Mendoza'),
	('Localidad 38', 'Mendoza'),
	('Localidad 39', 'Mendoza'),
	('Localidad 40', 'Misiones'),
	('Localidad 41', 'Misiones'),
	('Localidad 42', 'Misiones'),
	('Localidad 43', 'Neuquén'),
	('Localidad 44', 'Neuquén'),
	('Localidad 45', 'Neuquén'),
	('Localidad 46', 'Río Negro'),
	('Localidad 47', 'Río Negro'),
	('Localidad 48', 'Río Negro'),
	('Localidad 49', 'Salta'),
	('Localidad 50', 'Salta'),
	('Localidad 51', 'Salta'),
	('Localidad 52', 'San Juan'),
	('Localidad 53', 'San Juan'),
	('Localidad 54', 'San Juan'),
	('Localidad 55', 'San Luis'),
	('Localidad 56', 'San Luis'),
	('Localidad 57', 'San Luis'),
	('Localidad 58', 'Santa Cruz'),
	('Localidad 59', 'Santa Cruz'),
	('Localidad 60', 'Santa Cruz'),
	('Localidad 61', 'Santa Fe'),
	('Localidad 62', 'Santa Fe'),
	('Localidad 63', 'Santa Fe'),
	('Localidad 64', 'Santiago del Estero'),
	('Localidad 65', 'Santiago del Estero'),
	('Localidad 66', 'Santiago del Estero'),
	('Localidad 67', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'),
	('Localidad 68', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'),
	('Localidad 69', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'),
	('Localidad 70', 'Tucumán'),
	('Localidad 71', 'Tucumán'),
	('Localidad 72', 'Tucumán');

INSERT INTO persona(cuil, nombreyapellido, fecha_nacimiento) VALUES
	('20-10000000-01', 'Juan Perez',      '1990-05-15'),
	('20-20000000-02', 'Maria Rodriguez', '1985-12-03'),
	('20-30000000-03', 'Pedro Gomez',     '1995-02-28'),
	('20-40000000-04', 'Ana Fernandez',   '1998-09-20'),
	('20-50000000-05', 'Lucas Martinez',  '1980-07-10');

INSERT INTO chofer(cuil, antiguedad, sueldo) VALUES
	('20-10000000-01', 5,  20000),
	('20-20000000-02', 10, 30000),
	('20-30000000-03', 2,  15000);
	
INSERT INTO vehiculo(patente, modelo, marca, seguro, tipo) VALUES
	('ABC123', 'Fiesta',   'Ford',          'Allianz',    'Auto'),
	('DEF456', 'Hilux',    'Toyota',        'La Caja',    'Camion'),
	('GHI789', 'CBR600',   'Honda',         'Sancor',     'Moto'),
	('JKL012', 'Sprinter', 'Mercedes-Benz', 'Mapfre',     'Camion'),
	('MNO345', 'Civic',    'Honda',         'La Segunda', 'Auto'),
	('PQR678', 'R1',       'Yamaha',        'Provincia',  'Moto');

INSERT INTO camiones(patente, valor, kilometraje) VALUES
    ('DEF456', 75000,  80000),
    ('JKL012', 90000,  120000);

INSERT INTO choferes_camiones(cuil, patente) VALUES
	('20-10000000-01', 'DEF456'),
	('20-20000000-02', 'DEF456'),
	('20-20000000-02', 'JKL012');

INSERT INTO viaje(numero, patenteCamion, cuilChofer, kilometros, fechaInicio, fechaFin) VALUES
	(1, 'DEF456', '20-10000000-01', 300, TO_DATE('01-01-2017', 'DD-MM-YYYY'), TO_DATE('01-01-2023', 'DD-MM-YYYY'));

INSERT INTO viajeRecorrio(codigoViaje, codigoLocalidad) VALUES
	(1, 'Liniers'), 
	(1, 'Localidad 1'), 
	(1, 'Localidad 3'), 
	(1, 'Localidad 5'), 
	(1, 'Localidad 24');

INSERT INTO paquete(
	numViaje, valor, precioTranslado, 
	destinatarioCUIL, remitenteCUIL,
	entrega_localidad_codigo,
	entrega_direccion_calle,
	entrega_direccion_orientacion,
	entrega_direccion_numero
) VALUES
	(1, 300000, 5000, '20-30000000-01', '20-40000000-04', 1, 'Calle a', 'E', 3000); 

INSERT INTO viajeChoque(numeroChoque, provincia, codigoViaje) VALUES 
	();

INSERT INTO participoChoque(numeroChoque, provincia, patenteVehiculo) VALUES 
	();


-- USUARIOS
-- DBA: Debe tener acceso de lectura y escritura a toda la base de datos.
CREATE USER DBA WITH ENCRYPTED PASSWORD '1234';
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA PUBLIC TO DBA;

-- Gerente de la Empresa: Debe tener acceso de lectura a toda la base de datos.
CREATE USER GERENTE WITH ENCRYPTED PASSWORD '12345';
GRANT SELECT ON ALL TABLES IN SCHEMA PUBLIC TO GERENTE;

-- Jefe de Logística
CREATE USER JEFE_LOGISTICA WITH ENCRYPTED PASSWORD '12345678';
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE camiones, chofer, choferes_camiones, viaje, paquete, viajerecorrio TO JEFE_LOGISTICA;

-- CONSULTA PRIORITARIA (tenerla en cuenta para el diseño fisico de la BD)
-- Listado de paquetes (todos sus datos) ordenado por precio.
CREATE VIEW paquetes_ordenados AS (SELECT * FROM paquete ORDER BY valor);

-- 1. Paquetes (todos sus datos) ordenados por precio.
SELECT * FROM paquetes_ordenados;

-- 2. Choferes (todos los datos) que entregaron paquetes en Liniers (Buenos Aires).
SELECT * FROM chofer 
WHERE EXISTS (
	SELECT * FROM viaje
	WHERE viaje.cuilchofer=chofer.cuil AND
		EXISTS (
			SELECT * FROM viajerecorrio
			WHERE viajerecorrio.codigoviaje=viaje.numero AND
				EXISTS (
					SELECT * FROM localidad
					WHERE localidad.codigo=viajerecorrio.codigolocalidad AND
						localidad.nombre = 'Liniers' AND
						localidad.provincia = 'Buenos Aires'
				)
		)
)

SELECT chofer.* FROM chofer, viaje, viajerecorrio, localidad WHERE
	chofer.cuil = viaje.cuilchofer AND
	viajerecorrio.codigoviaje = viaje.numero AND 
	localidad.codigo = viajerecorrio.codigolocalidad AND
	localidad.nombre = 'Liniers' AND
	localidad.provincia = 'Buenos Aires';

-- 3. Choferes (todos los datos) que participaron en accidentes en el año 2022 y también en el 2023.
SELECT * FROM chofer
WHERE EXISTS (
	(SELECT numero, provincia FROM actachoque WHERE year(fecha) = 2022)
	INTERSECT
	(SELECT numero, provincia FROM viajeChoque WHERE EXISTS (
		SELECT * FROM viaje
		WHERE viaje.numero =viajeChoque.codigoviaje AND
			viaje.cuilchofer=chofer.cuil
	))
) AND EXISTS (
	(SELECT numero, provincia FROM actachoque WHERE year(fecha) = 2023)
	INTERSECT
	(SELECT numero, provincia FROM viajeChoque WHERE EXISTS (
		SELECT * FROM viaje
		WHERE viaje.numero =viajeChoque.codigoviaje AND
			viaje.cuilchofer=chofer.cuil
	))
)

-- another solution
SELECT * FROM chofer
WHERE EXISTS (
	SELECT * FROM viaje
	WHERE viaje.cuilchofer=chofer.cuil AND
		EXISTS (
			SELECT * FROM viajechoque
			WHERE viajechoque.codigoviaje=viaje.numero AND
				EXISTS (
					SELECT * FROM actachoque
					WHERE actachoque.numero=viajechoque.numero AND
						year(actachoque.fecha) = 2022
				)
		)
) AND EXISTS (
	SELECT * FROM viaje
	WHERE viaje.cuilchofer=chofer.cuil AND
		EXISTS (
			SELECT * FROM viajechoque
			WHERE viajechoque.codigoviaje=viaje.numero AND
				EXISTS (
					SELECT * FROM actachoque
					WHERE actachoque.numero=viajechoque.numero AND
						year(actachoque.fecha) = 2023
				)
		)
)

-- 4. Localidades a las que no se hicieron envíos durante 2022.
SELECT * FROM localidad
WHERE NOT EXISTS (
	SELECT * FROM viaje
	WHERE EXISTS (
		SELECT * FROM viajerecorrio
		WHERE viajerecorrio.codigoviaje = viaje.numero AND
			viajerecorrio.codigolocalidad = localidad.codigo AND
			year(viaje.fechainicio) = 2022
	)
)

-- 5. Choferes (todos los datos) que realizaron más viajes.
SELECT cuilchofer FROM viaje
GROUP BY cuilchofer
HAVING COUNT(*)=(
	SELECT COUNT() FROM viaje GROUP BY cuilchofer ORDER BY COUNT() LIMIT 1
)

-- 6. Camiones (todos los datos) que fueron (entregaron paquetes) a todas las localidades de Buenos Aires.
SELECT * FROM camiones
WHERE NOT EXISTS (
	SELECT * FROM localidad
	WHERE provincia = 'Buenos Aires' AND
		NOT EXISTS (
			SELECT * FROM viaje
			WHERE viaje.patentecamion = camiones.patente AND
				EXISTS (
					SELECT * FROM viajerecorrio
					WHERE viajerecorrio.codigoviaje = viaje.numero AND
						viajerecorrio.codigolocalidad = localidad.codigo
				)
		)
)