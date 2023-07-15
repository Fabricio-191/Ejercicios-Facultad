-- SPRT2022
/* Para borrar todos los datos
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
DROP USER IF EXISTS DBA;
DROP USER IF EXISTS GERENTE;
DROP USER IF EXISTS JEFE_LOGISTICA;
*/


CREATE TYPE TIPO_VEHICULO AS ENUM ('Camion', 'Auto', 'Moto');
CREATE TYPE ORIENTACION AS ENUM ('N', 'S', 'E', 'O');

CREATE DOMAIN PATENTE AS TEXT CHECK (value ~ '^[A-Z]{3}[0-9]{3}$' OR value ~ '^[A-Z]{2}[0-9]{3}[A-Z]{2}$');
CREATE DOMAIN CUIL AS TEXT CHECK (value ~ '^[0-9]{2}-[0-9]{1,9}-[0-9]{1,2}$');

CREATE TABLE IF NOT EXISTS vehiculos (
    patente PATENTE PRIMARY KEY,
    modelo TEXT NOT NULL,
    marca  TEXT NOT NULL,
    seguro TEXT NOT NULL,
    tipo TIPO_VEHICULO NOT NULL
    -- tipo TEXT NOT NULL CHECK(tipo IN ('Camion', 'Auto', 'Moto'))
);

CREATE TABLE IF NOT EXISTS camiones (
    patente PATENTE PRIMARY KEY REFERENCES vehiculos(patente) ON DELETE CASCADE ON UPDATE CASCADE,
    valor REAL NOT NULL CHECK (valor >= 0),
    kilometraje REAL NOT NULL CHECK (kilometraje >= 0)
);

CREATE TABLE IF NOT EXISTS personas (
    cuil CUIL PRIMARY KEY,
    nombre_apellido TEXT NOT NULL,
    domicilio_calle TEXT NOT NULL,
	domicilio_orientacion ORIENTACION NOT NULL,
	domicilio_numero INT NOT NULL
    -- fecha_nacimiento DATE NOT NULL CHECK (fecha_nacimiento < CURRENT_DATE AND fecha_nacimiento > '1900-01-01')
);

CREATE TABLE IF NOT EXISTS choferes (
    cuil CUIL PRIMARY KEY,
    antiguedad REAL NOT NULL CHECK (antiguedad >= 0),
    sueldo REAL NOT NULL CHECK (sueldo >= 0)
);

CREATE TABLE IF NOT EXISTS choferes_camiones (
    cuil CUIL REFERENCES choferes(cuil) ON DELETE CASCADE ON UPDATE CASCADE,
    patente TEXT REFERENCES camiones(patente) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (cuil, patente)
);

CREATE TABLE IF NOT EXISTS provincias (nombre TEXT PRIMARY KEY);

CREATE TABLE IF NOT EXISTS localidades (
    codigo SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    provincia TEXT NOT NULL REFERENCES provincias(nombre) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS viaje (
    numero INT PRIMARY KEY,
    patente_camion TEXT NOT NULL,
    cuil_chofer CUIL NOT NULL,
    kilometros REAL NOT NULL CHECK (kilometros > 0),
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL CHECK (fecha_inicio < fecha_fin),
    FOREIGN KEY (patente_camion, cuil_chofer) REFERENCES choferes_camiones(patente, cuil)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS viaje_recorrio (
    codigo_viaje     INT NOT NULL REFERENCES viaje(numero),
    codigo_localidad INT NOT NULL REFERENCES localidades(codigo),
    fecha_hora TIMESTAMP NOT NULL CHECK (fecha_hora < CURRENT_TIMESTAMP),
    PRIMARY KEY (codigo_localidad, codigo_viaje, fecha_hora)
);

CREATE TABLE IF NOT EXISTS paquetes (
    numero SERIAL PRIMARY KEY,
    codigo_viaje INT NOT NULL REFERENCES viaje(numero) ON DELETE CASCADE ON UPDATE CASCADE,
    valor REAL NOT NULL CHECK (valor > 0),
    precio_translado REAL NOT NULL CHECK (precio_translado > 0),
    destinatario_CUIL CUIL NOT NULL,
    remitente_CUIL CUIL NOT NULL REFERENCES personas(cuil) ON DELETE CASCADE ON UPDATE CASCADE,
    entrega_localidad_codigo INT NOT NULL REFERENCES localidades(codigo) ON DELETE CASCADE ON UPDATE CASCADE,
    entrega_direccion_calle TEXT NOT NULL,
    entrega_direccion_orientacion ORIENTACION NOT NULL,
    entrega_direccion_numero INT NOT NULL
    -- FOREIGN KEY (codigo_viaje, entrega_localidad_codigo) REFERENCES viaje_recorrio(codigo_viaje, codigo_localidad)
    --     ON DELETE CASCADE
    --     ON UPDATE CASCADE
	-- Esa clave foranea no la pudimos agregar dado que puede repetirse varias veces el codigo_viaje y el codigo_localidad en la tabla viaje_recorrio con distinta fecha_hora
);

CREATE TABLE IF NOT EXISTS choques (
    numero    INT  NOT NULL,
    provincia TEXT NOT NULL REFERENCES provincias(nombre) ON DELETE CASCADE ON UPDATE CASCADE,
    fecha     DATE NOT NULL CHECK (fecha < CURRENT_DATE),
    costo     REAL NOT NULL CHECK (costo > 0),
    descripcion TEXT NOT NULL,
	viaje INT REFERENCES viaje(numero) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (numero, provincia)
);

CREATE TABLE IF NOT EXISTS participo_choque (
    numero_choque    INT     NOT NULL,
    provincia_choque TEXT    NOT NULL,
    patente_vehiculo PATENTE NOT NULL REFERENCES vehiculos(patente) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (numero_choque, provincia_choque, patente_vehiculo),
    FOREIGN KEY (numero_choque, provincia_choque) REFERENCES choques(numero, provincia)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO provincias(nombre) VALUES
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

INSERT INTO localidades(nombre, provincia) VALUES
    ('localidades 1' , 'Buenos Aires'                   ),
    ('Liniers'       , 'Buenos Aires'                   ),
    ('localidades 3' , 'Buenos Aires'                   ),
    ('localidades 4' , 'Ciudad Autónoma de Buenos Aires'),
    ('localidades 5' , 'Ciudad Autónoma de Buenos Aires'),
    ('localidades 6' , 'Ciudad Autónoma de Buenos Aires'),
    ('localidades 7' , 'Catamarca'),
    ('localidades 8' , 'Catamarca'),
    ('localidades 9' , 'Catamarca'),
    ('localidades 10', 'Chaco'),
    ('localidades 11', 'Chaco'),
    ('localidades 12', 'Chaco'),
    ('localidades 13', 'Chubut'),
    ('localidades 14', 'Chubut'),
    ('localidades 15', 'Chubut'),
    ('localidades 16', 'Córdoba'),
    ('localidades 17', 'Córdoba'),
    ('localidades 18', 'Córdoba'),
    ('localidades 19', 'Corrientes'),
    ('localidades 20', 'Corrientes'),
    ('localidades 21', 'Corrientes'),
    ('localidades 22', 'Entre Ríos'),
    ('localidades 23', 'Entre Ríos'),
    ('localidades 24', 'Entre Ríos'),
    ('localidades 25', 'Formosa'),
    ('localidades 26', 'Formosa'),
    ('localidades 27', 'Formosa'),
    ('localidades 28', 'Jujuy'),
    ('localidades 29', 'Jujuy'),
    ('localidades 30', 'Jujuy'),
    ('localidades 31', 'La Pampa'),
    ('localidades 32', 'La Pampa'),
    ('localidades 33', 'La Pampa'),
    ('localidades 34', 'La Rioja'),
    ('localidades 35', 'La Rioja'),
    ('localidades 36', 'La Rioja'),
    ('localidades 37', 'Mendoza'),
    ('localidades 38', 'Mendoza'),
    ('localidades 39', 'Mendoza'),
    ('localidades 40', 'Misiones'),
    ('localidades 41', 'Misiones'),
    ('localidades 42', 'Misiones'),
    ('localidades 43', 'Neuquén'),
    ('localidades 44', 'Neuquén'),
    ('localidades 45', 'Neuquén'),
    ('localidades 46', 'Río Negro'),
    ('localidades 47', 'Río Negro'),
    ('localidades 48', 'Río Negro'),
    ('localidades 49', 'Salta'),
    ('localidades 50', 'Salta'),
    ('localidades 51', 'Salta'),
    ('localidades 52', 'San Juan'),
    ('localidades 53', 'San Juan'),
    ('localidades 54', 'San Juan'),
    ('localidades 55', 'San Luis'),
    ('localidades 56', 'San Luis'),
    ('localidades 57', 'San Luis'),
    ('localidades 58', 'Santa Cruz'),
    ('localidades 59', 'Santa Cruz'),
    ('localidades 60', 'Santa Cruz'),
    ('localidades 61', 'Santa Fe'),
    ('localidades 62', 'Santa Fe'),
    ('localidades 63', 'Santa Fe'),
    ('localidades 64', 'Santiago del Estero'),
    ('localidades 65', 'Santiago del Estero'),
    ('localidades 66', 'Santiago del Estero'),
    ('localidades 67', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'),
    ('localidades 68', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'),
    ('localidades 69', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'),
    ('localidades 70', 'Tucumán'),
    ('localidades 71', 'Tucumán'),
    ('localidades 72', 'Tucumán');

INSERT INTO personas(cuil, nombre_apellido, domicilio_calle, domicilio_orientacion, domicilio_numero) VALUES
    ('20-10000000-01', 'Juan Perez',        'A', 'O', 123),
    ('20-20000000-02', 'Maria Rodriguez',   'B', 'N', 781),
    ('20-30000000-03', 'Pedro Gomez',       'C', 'S', 456),
    ('20-40000000-04', 'Ana Fernandez',     'D', 'E', 8241),
    ('20-50000000-05', 'Lucas Martinez',    'E', 'N', 23),
    ('20-60000000-06', 'Carla Sanchez',     'F', 'N', 504),
    ('20-70000000-07', 'Jose Gonzalez',     'G', 'O', 612),
    ('20-80000000-08', 'Sofia Lopez',       'H', 'S', 72),
    ('20-90000000-09', 'Carlos Diaz',       'I', 'S', 585),
    ('20-10000000-10', 'Florencia Perez',   'J', 'E', 813),
    ('20-11000000-11', 'Martin Rodriguez',  'K', 'O', 1153),
    ('20-12000000-12', 'Valentina Gomez',   'L', 'O', 13),
    ('20-13000000-13', 'Agustin Fernandez', 'M', 'O', 941);

INSERT INTO choferes(cuil, antiguedad, sueldo) VALUES
    ('20-10000000-01', 5,  20000),
    ('20-20000000-02', 10, 30000),
    ('20-30000000-03', 2,  15000),
    ('20-40000000-04', 1,  10000),
    ('20-50000000-05', 3,  18000),
    ('20-60000000-06', 4,  25000);

INSERT INTO vehiculos(patente, modelo, marca, seguro, tipo) VALUES
    ('ABC123', 'Fiesta',        'Ford',          'Allianz',    'Auto'  ),
    ('DEF456', 'Sprinter',      'Mercedes-Benz', 'Mapfre',     'Camion'),
    ('JKL012', 'Hilux',         'Toyota',        'La Caja',    'Camion'),
    ('LPQ310', 'Tornado',       'Chevrolet',     'Sancor',     'Camion'),
    ('REP120', 'Tornado',       'Chevrolet',     'Sancor',     'Camion'),
    ('MIL210', 'Tornado',       'Chevrolet',     'Sancor',     'Camion'),
    ('PQR678', 'FZ16',          'Yamaha',        'Provincia',  'Camion'),
    ('STU901', 'Corolla',       'Toyota',        'La Segunda', 'Camion'),
    ('VWX234', 'CBR1000',       'Honda',         'Allianz',    'Camion'),
    ('QPR310', 'CBR1000',       'Honda',         'Allianz',    'Camion'),
    ('GHI789', 'CBR600',        'Honda',         'Sancor',     'Moto'  ),
    ('MLO456', 'Civic',         'Honda',         'La Segunda', 'Auto'  ),
    ('MNO345', 'Constellation', 'Volkswagen',    'Mapfre',     'Camion'),
    ('IOE450', 'R1',            'Yamaha',        'Provincia',  'Moto'  );

INSERT INTO camiones(patente, valor, kilometraje) VALUES
    ('DEF456', 75000,  80000 ),
    ('JKL012', 90000,  120000),
    ('MNO345', 50000,  50000 ),
    ('PQR678', 100000, 100000),
    ('STU901', 150000, 150000),
    ('VWX234', 200000, 200000);

INSERT INTO choferes_camiones(cuil, patente) VALUES
    ('20-10000000-01', 'DEF456'),
    ('20-20000000-02', 'MNO345'),
    ('20-30000000-03', 'JKL012'),
    ('20-40000000-04', 'VWX234'),
    ('20-50000000-05', 'PQR678');

INSERT INTO viaje(numero, patente_camion, cuil_chofer, kilometros, fecha_inicio, fecha_fin) VALUES
    (1, 'DEF456', '20-10000000-01', 1000, TO_DATE('01-01-2022', 'DD-MM-YYYY'), TO_DATE('05-02-2022', 'DD-MM-YYYY')),
    (2, 'MNO345', '20-20000000-02', 4000, TO_DATE('02-02-2022', 'DD-MM-YYYY'), TO_DATE('30-03-2022', 'DD-MM-YYYY')),
    (3, 'VWX234', '20-40000000-04', 3000, TO_DATE('15-03-2022', 'DD-MM-YYYY'), TO_DATE('02-08-2022', 'DD-MM-YYYY')),
    (4, 'DEF456', '20-10000000-01', 2000, TO_DATE('20-04-2023', 'DD-MM-YYYY'), TO_DATE('04-05-2023', 'DD-MM-YYYY')),
    (5, 'MNO345', '20-20000000-02', 5000, TO_DATE('01-05-2023', 'DD-MM-YYYY'), TO_DATE('13-06-2023', 'DD-MM-YYYY'));

INSERT INTO viaje_recorrio(codigo_viaje, codigo_localidad, fecha_hora) VALUES
    (1, 1,  TO_DATE('08-01-2022', 'DD-MM-YYYY')), 
    (1, 2,  TO_DATE('12-01-2022', 'DD-MM-YYYY')), 
    (1, 3,  TO_DATE('16-01-2022', 'DD-MM-YYYY')), 
    (1, 4,  TO_DATE('21-01-2022', 'DD-MM-YYYY')), 
    (2, 5,  TO_DATE('14-02-2022', 'DD-MM-YYYY')), 
    (2, 6,  TO_DATE('18-03-2022', 'DD-MM-YYYY')),
    (2, 7,  TO_DATE('19-03-2022', 'DD-MM-YYYY')),
    (3, 15, TO_DATE('02-05-2022', 'DD-MM-YYYY')),
    (4, 25, TO_DATE('26-04-2023', 'DD-MM-YYYY')),
    (5, 35, TO_DATE('15-05-2023', 'DD-MM-YYYY'));

INSERT INTO paquetes(
    codigo_viaje, valor, precio_translado, 
    destinatario_CUIL, remitente_CUIL,
    entrega_localidad_codigo,
    entrega_direccion_calle,
    entrega_direccion_orientacion,
    entrega_direccion_numero
) VALUES
    (1, 3000,   5000,  '20-30000000-01', '20-30000000-03', 1,  'Calle a', 'E', 3000),
    (1, 500000, 10000, '20-10000000-01', '20-40000000-04', 2,  'Calle b', 'N', 600 ),
    (1, 2000,   2000,  '20-80000000-08', '20-90000000-09', 3,  'Calle c', 'S', 100 ),
    (1, 20000,  3000,  '20-70000000-07', '20-80000000-08', 4,  'Calle d', 'O', 200 ),
    (2, 4000,   4000,  '20-90000000-09', '20-10000000-10', 5,  'Calle e', 'N', 300 ),
    (2, 5000,   4000,  '20-10000000-10', '20-11000000-11', 6,  'Calle f', 'S', 300 ),
    (3, 10000,  4000,  '20-11000000-11', '20-12000000-12', 15, 'Calle g', 'O', 400 ),
    (4, 50000,  4000,  '20-12000000-12', '20-13000000-13', 25, 'Calle h', 'S', 500 ),
    (5, 3000,   4000,  '20-13000000-13', '20-11000000-11', 35, 'Calle i', 'N', 600 );

INSERT INTO choques(numero, provincia, fecha, costo, descripcion, viaje) VALUES 
    (1, 'Buenos Aires', TO_DATE('01-02-2022', 'DD-MM-YYYY'), 30000, '-', 1),
    (2, 'Buenos Aires', TO_DATE('02-02-2022', 'DD-MM-YYYY'), 40000, '-', 2),
    (1, 'Mendoza',      TO_DATE('23-04-2023', 'DD-MM-YYYY'), 70000, '-', 4);

INSERT INTO participo_choque(numero_choque, provincia_choque, patente_vehiculo) VALUES
    (1, 'Buenos Aires', 'DEF456'),
    (1, 'Buenos Aires', 'REP120'),
    (2, 'Buenos Aires', 'MNO345'),
    (2, 'Buenos Aires', 'JKL012'),
    (2, 'Buenos Aires', 'GHI789'),
    (1, 'Mendoza',      'DEF456'),
    (1, 'Mendoza',      'PQR678'),
    (1, 'Mendoza',      'IOE450');

-- USUARIOS
CREATE USER DBA WITH ENCRYPTED PASSWORD '9yJXiIREMGVbDQHfsmhWk8BGJ';
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA PUBLIC TO DBA;

CREATE USER GERENTE WITH ENCRYPTED PASSWORD 'QTreNZm23DJZ7hM';
GRANT SELECT ON ALL TABLES IN SCHEMA PUBLIC TO GERENTE;

CREATE USER JEFE_LOGISTICA WITH ENCRYPTED PASSWORD 'zzRSf9l7TaOU48sFMowM';
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE camiones, choferes, choferes_camiones, viaje, paquetes, viaje_recorrio TO JEFE_LOGISTICA;
-- Jefe de Logística: Debe tener acceso de lectura y escritura a todos los datos relativos a los camioneros, camiones y viajes.
-- Esto obviamente incluye las tablas camiones, choferes, choferes_camiones, viaje
-- Pero consideramos que tambien debia tener acceso a las tablas paquetes y viaje_recorrio dado que estan muy relacionadas a las otras, ademas de que es justamente el jefe de logistica


-- CONSULTAS

-- CONSULTA PRIORITARIA (tenerla en cuenta para el diseño fisico de la BD)
-- Listado de paquetes (todos sus datos) ordenado por precio.

CREATE INDEX IF NOT EXISTS paquetes_ordenados_valor ON paquetes(valor DESC);

-- 1. Listado de paquetes (todos sus datos) ordenado por precio.
SELECT * FROM paquetes ORDER BY valor DESC;

-- 2. Choferes (todos los datos) que entregaron paquetes en Liniers (Buenos Aires).

SELECT * FROM personas NATURAL JOIN (
	SELECT choferes.*
	FROM choferes
		JOIN viaje ON choferes.cuil = viaje.cuil_chofer
		JOIN paquetes ON paquetes.codigo_viaje = viaje.numero
		JOIN localidades ON paquetes.entrega_localidad_codigo = localidades.codigo
	WHERE localidades.nombre = 'Liniers' AND localidades.provincia = 'Buenos Aires'
) AS choferes_liniers


-- 3. Choferes (todos los datos) que participaron en accidentes en el año 2022 y también en el 2023.



SELECT *
FROM choferes NATURAL JOIN personas NATURAL JOIN (
	SELECT choferes.cuil
	FROM choferes
		JOIN viaje ON choferes.cuil = viaje.cuil_chofer
		JOIN choques ON choques.viaje = viaje.numero
	WHERE EXTRACT(YEAR FROM choques.fecha) = 2022
) AS choferes_2022 NATURAL JOIN (
	SELECT choferes.cuil
	FROM choferes
		JOIN viaje ON choferes.cuil = viaje.cuil_chofer
		JOIN choques ON choques.viaje = viaje.numero
	WHERE EXTRACT(YEAR FROM choques.fecha) = 2023
) AS choferes_2023


-- 4. Localidades a las que no se hicieron envíos durante 2022.
SELECT * FROM localidades WHERE NOT EXISTS (
	SELECT *
	FROM paquetes JOIN viaje_recorrio ON paquetes.codigo_viaje = viaje_recorrio.codigo_viaje
	WHERE paquetes.entrega_localidad_codigo = localidades.codigo AND
		EXTRACT(YEAR FROM viaje_recorrio.fecha_hora) = 2022
);

-- 5. Choferes (todos los datos) que realizaron más viajes.
SELECT *
FROM personas NATURAL JOIN choferes NATURAL JOIN (
    SELECT cuil_chofer AS cuil
    FROM viaje
    GROUP BY cuil_chofer
    HAVING COUNT(*) = (
        SELECT COUNT(*) FROM viaje GROUP BY cuil_chofer ORDER BY COUNT(*) DESC LIMIT 1
    )
) AS choferes_mas_viajes;

-- 6. Camiones (todos los datos) que fueron (entregaron paquetes) a todas las localidades de Buenos Aires.
SELECT * FROM camiones NATURAL JOIN vehiculos
WHERE NOT EXISTS (
    SELECT * FROM localidades
    WHERE provincia = 'Buenos Aires' AND NOT EXISTS (
        SELECT *
		FROM viaje JOIN paquetes ON paquetes.codigo_viaje = viaje.numero
        WHERE viaje.patente_camion = camiones.patente AND
			paquetes.entrega_localidad_codigo = localidades.codigo
    )
)
