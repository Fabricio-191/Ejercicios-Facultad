-- SPRT2022

CREATE TYPE TIPO_VEHICULO AS ENUM ('Camion', 'Auto', 'Moto');

CREATE TABLE IF NOT EXISTS vehiculo (
    patente TEXT PRIMARY KEY,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    seguro TEXT NOT NULL,
    tipo TIPO_VEHICULO NOT NULL,
)

CREATE TABLE IF NOT EXISTS camiones {
    patente TEXT PRIMARY KEY REFERENCES vehiculo(patente),
    valor INT NOT NULL CHECK (valor > 0),
    kilometraje INT NOT NULL CHECK (kilometraje > 0),
}

CREATE TABLE IF NOT EXISTS persona {
    cuil TEXT PRIMARY KEY,
    nombreyapellido TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL,
}

CREATE TABLE IF NOT EXISTS chofer (
    cuil TEXT PRIMARY KEY,
    antiguedad INT NOT NULL CHECK (antiguedad > 0),
    sueldo REAL NOT NULL CHECK (sueldo > 0),
)

CREATE TABLE IF NOT EXISTS choferes_camiones (
    cuil TEXT NOT NULL REFERENCES chofer(cuil),
    patente TEXT NOT NULL REFERENCES camiones(patente)
    PRIMARY KEY (cuil, patente)
)

CREATE TABLE IF NOT EXISTS provincia (
    nombre TEXT PRIMARY KEY
)

CREATE TABLE IF NOT EXISTS localidad (
    codigo INT PRIMARY KEY,
    nombre TEXT NOT NULL,
    provincia TEXT NOT NULL REFERENCES provincia(nombre)
)

CREATE TABLE IF NOT EXISTS actaChoque (
    numero INT,
    provincia TEXT NOT NULL  REFERENCES provincia(nombre),
    fecha DATE NOT NULL CHECK (fecha < CURRENT_DATE),
    costo REAL NOT NULL CHECK (costo > 0),
    descripcion TEXT NOT NULL,
	PRIMARY KEY (numero, provincia)
)

CREATE TABLE IF NOT EXISTS viaje (
    numero INT PRIMARY KEY,
    patenteCamion TEXT NOT NULL REFERENCES camiones(patente),
    cuilChofer TEXT NOT NULL REFERENCES chofer(cuil),
    kilometros REAL NOT NULL CHECK (kilometros > 0),
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL CHECK (fechaFin > fechaInicio),
)

CREATE TABLE IF NOT EXISTS paquete (
    numero INT PRIMARY KEY,
    valor REAL NOT NULL CHECK (valor > 0),
    precioTranslado REAL NOT NULL CHECK (precioTranslado > 0),
    destinatarioCUIL TEXT NOT NULL,
    remitenteCUIL TEXT NOT NULL REFERENCES persona(cuil) ON DELETE CASCADE ON UPDATE CASCADE,
    codigoLocalidadEntrega INT NOT NULL REFERENCES localidad(codigo),
    calleDireccionEntrega TEXT NOT NULL,
    orientacionDireccionEntrega TEXT NOT NULL,
    numeroDireccionEntrega INT NOT NULL,
    numViaje INT NOT NULL REFERENCES viaje(numero)
)

CREATE TABLE IF NOT EXISTS viajeRecorrio (
    codigoLocalidad INT REFERENCES localidad(codigo),
    codigoViaje INT REFERENCES viaje(numero),
    PRIMARY KEY (codigoLocalidad, codigoViaje)
)

CREATE TABLE IF NOT EXISTS participoChoque (
    numeroChoque INT REFERENCES actaChoque(numero),
    patenteVehiculo TEXT REFERENCES vehiculo(patente),
    PRIMARY KEY (numeroChoque, patenteVehiculo)
)

CREATE TABLE IF NOT EXISTS viajeChoque (
    numeroChoque INT REFERENCES actaChoque(numero),
    codigoViaje INT REFERENCES viaje(numero)
    PRIMARY KEY (numeroChoque, codigoViaje)
)

-- generate a dataset

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
	('Localidad 2', 'Buenos Aires'),
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

INSERT INTO choferes_camiones(cuil, patente) VALUES
	('20-10000000-01', 'DEF456'),
	('20-20000000-02', 'DEF456'),
	('20-20000000-02', 'JKL012');

INSERT INTO actaChoque(provincia, fecha, costo, descripcion) VALUES
	('Buenos Aires', '2019-01-01', 10000, 'Choque en la ruta 1'),
	('Buenos Aires', '2020-02-02', 20000, 'Choque en la ruta 2'),
	('Buenos Aires', '2021-03-03', 30000, 'Choque en la ruta 3')
