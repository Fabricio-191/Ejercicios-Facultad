-- SPRT2022
DROP USER IF EXISTS DBA;
DROP USER IF EXISTS GERENTE;
DROP USER IF EXISTS JEFE_LOGISTICA;
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;


CREATE TYPE TIPO_VEHICULO AS ENUM ('Camion', 'Auto', 'Moto');
CREATE TYPE ORIENTACION AS ENUM ('N', 'S', 'E', 'O');

CREATE DOMAIN PATENTE AS TEXT CHECK (value ~ '^[A-Z]{3}[0-9]{3}$' OR value ~ '^[A-Z]{2}[0-9]{3}[A-Z]{2}$');
CREATE DOMAIN CUIL AS TEXT CHECK (value ~ '^[0-9]{2}-[0-9]{1,9}-[0-9]{1,2}$');

CREATE TABLE IF NOT EXISTS vehiculo (
    patente PATENTE PRIMARY KEY,
    modelo TEXT NOT NULL CHECK (modelo != ''),
    marca  TEXT NOT NULL CHECK (marca  != ''),
    seguro TEXT NOT NULL CHECK (seguro != ''),
    tipo TIPO_VEHICULO NOT NULL
    -- tipo TEXT NOT NULL CHECK(tipo IN ('Camion', 'Auto', 'Moto'))
);

CREATE TABLE IF NOT EXISTS camiones (
    patente PATENTE PRIMARY KEY REFERENCES vehiculo(patente) ON DELETE CASCADE ON UPDATE CASCADE,
    valor INT NOT NULL CHECK (valor > 0),
    kilometraje INT NOT NULL CHECK (kilometraje > 0)
);

CREATE TABLE IF NOT EXISTS persona (
    cuil CUIL PRIMARY KEY,
    nombre_apellido TEXT NOT NULL CHECK (nombre_apellido != ''),
    domicilio TEXT NOT NULL CHECK (domicilio != '')
    -- fecha_nacimiento DATE NOT NULL CHECK (fecha_nacimiento < CURRENT_DATE AND fecha_nacimiento > '1900-01-01')
);

CREATE TABLE IF NOT EXISTS chofer (
    cuil CUIL PRIMARY KEY,
    antiguedad INT NOT NULL CHECK (antiguedad > 0),
    sueldo REAL NOT NULL CHECK (sueldo > 0)
);

CREATE TABLE IF NOT EXISTS choferes_camiones (
    cuil CUIL NOT NULL REFERENCES chofer(cuil) ON DELETE CASCADE ON UPDATE CASCADE,
    patente TEXT NOT NULL REFERENCES camiones(patente) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (cuil, patente)
);

CREATE TABLE IF NOT EXISTS provincia (nombre TEXT PRIMARY KEY);

CREATE TABLE IF NOT EXISTS localidad (
    codigo SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    provincia TEXT NOT NULL REFERENCES provincia(nombre) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS viaje (
    numero INT PRIMARY KEY,
    patente_camion TEXT NOT NULL REFERENCES camiones(patente) ON DELETE CASCADE ON UPDATE CASCADE,
    cuil_chofer CUIL NOT NULL REFERENCES chofer(cuil) ON DELETE CASCADE ON UPDATE CASCADE,
    kilometros REAL NOT NULL CHECK (kilometros > 0),
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL CHECK (fecha_inicio < fecha_fin),
    FOREIGN KEY (patente_camion, cuil_chofer) REFERENCES choferes_camiones(patente, cuil)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS viaje_recorrio (
    codigo_viaje     INT NOT NULL REFERENCES viaje(numero),
    codigo_localidad INT NOT NULL REFERENCES localidad(codigo),
    fecha_hora TIMESTAMP NOT NULL CHECK (fecha_hora < CURRENT_TIMESTAMP),
    PRIMARY KEY (codigo_localidad, codigo_viaje, fecha_hora)
);

CREATE TABLE IF NOT EXISTS paquete (
    numero SERIAL PRIMARY KEY,
    codigo_viaje INT NOT NULL REFERENCES viaje(numero) ON DELETE CASCADE ON UPDATE CASCADE,
    valor REAL NOT NULL CHECK (valor > 0),
    precio_translado REAL NOT NULL CHECK (precio_translado > 0),
    destinatario_CUIL CUIL NOT NULL,
    remitente_CUIL CUIL NOT NULL REFERENCES persona(cuil) ON DELETE CASCADE ON UPDATE CASCADE,
    entrega_localidad_codigo INT NOT NULL REFERENCES localidad(codigo) ON DELETE CASCADE ON UPDATE CASCADE,
    entrega_direccion_calle TEXT NOT NULL,
    entrega_direccion_orientacion ORIENTACION NOT NULL,
    entrega_direccion_numero INT NOT NULL
    -- FOREIGN KEY (codigo_viaje, entrega_localidad_codigo) REFERENCES viaje_recorrio(codigo_viaje, codigo_localidad)
    --     ON DELETE CASCADE
    --     ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS choque (
    numero INT     NOT NULL,
    provincia TEXT NOT NULL REFERENCES provincia(nombre) ON DELETE CASCADE ON UPDATE CASCADE,
    fecha     DATE NOT NULL CHECK (fecha < CURRENT_DATE),
    costo     REAL NOT NULL CHECK (costo > 0),
    descripcion TEXT NOT NULL,
    PRIMARY KEY (numero, provincia)
);

CREATE TABLE IF NOT EXISTS participo_choque (
    numero_choque INT        NOT NULL,
    provincia_choque TEXT    NOT NULL REFERENCES provincia(nombre) ON DELETE CASCADE ON UPDATE CASCADE,
    patente_vehiculo PATENTE NOT NULL REFERENCES vehiculo(patente) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (numero_choque, provincia_choque, patente_vehiculo),
    FOREIGN KEY (numero_choque, provincia_choque) REFERENCES choque(numero, provincia)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS viaje_choque (
    numero_choque INT,
    provincia_choque TEXT NOT NULL REFERENCES provincia(nombre) ON DELETE CASCADE ON UPDATE CASCADE,
    codigo_viaje INT REFERENCES viaje(numero) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (numero_choque, provincia_choque, codigo_viaje),
    FOREIGN KEY (numero_choque, provincia_choque) REFERENCES choque(numero, provincia)
        ON DELETE CASCADE
        ON UPDATE CASCADE
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
    ('Localidad 1' , 'Buenos Aires'                                         ),
    ('Liniers'     , 'Buenos Aires'                                         ),
    ('Localidad 3' , 'Buenos Aires'                                         ),
    ('Localidad 4' , 'Ciudad Autónoma de Buenos Aires'                      ),
    ('Localidad 5' , 'Ciudad Autónoma de Buenos Aires'                      ),
    ('Localidad 6' , 'Ciudad Autónoma de Buenos Aires'                      ),
    ('Localidad 7' , 'Catamarca'                                            ),
    ('Localidad 8' , 'Catamarca'                                            ),
    ('Localidad 9' , 'Catamarca'                                            ),
    ('Localidad 10', 'Chaco'                                                ),
    ('Localidad 11', 'Chaco'                                                ),
    ('Localidad 12', 'Chaco'                                                ),
    ('Localidad 13', 'Chubut'                                               ),
    ('Localidad 14', 'Chubut'                                               ),
    ('Localidad 15', 'Chubut'                                               ),
    ('Localidad 16', 'Córdoba'                                              ),
    ('Localidad 17', 'Córdoba'                                              ),
    ('Localidad 18', 'Córdoba'                                              ),
    ('Localidad 19', 'Corrientes'                                           ),
    ('Localidad 20', 'Corrientes'                                           ),
    ('Localidad 21', 'Corrientes'                                           ),
    ('Localidad 22', 'Entre Ríos'                                           ),
    ('Localidad 23', 'Entre Ríos'                                           ),
    ('Localidad 24', 'Entre Ríos'                                           ),
    ('Localidad 25', 'Formosa'                                              ),
    ('Localidad 26', 'Formosa'                                              ),
    ('Localidad 27', 'Formosa'                                              ),
    ('Localidad 28', 'Jujuy'                                                ),
    ('Localidad 29', 'Jujuy'                                                ),
    ('Localidad 30', 'Jujuy'                                                ),
    ('Localidad 31', 'La Pampa'                                             ),
    ('Localidad 32', 'La Pampa'                                             ),
    ('Localidad 33', 'La Pampa'                                             ),
    ('Localidad 34', 'La Rioja'                                             ),
    ('Localidad 35', 'La Rioja'                                             ),
    ('Localidad 36', 'La Rioja'                                             ),
    ('Localidad 37', 'Mendoza'                                              ),
    ('Localidad 38', 'Mendoza'                                              ),
    ('Localidad 39', 'Mendoza'                                              ),
    ('Localidad 40', 'Misiones'                                             ),
    ('Localidad 41', 'Misiones'                                             ),
    ('Localidad 42', 'Misiones'                                             ),
    ('Localidad 43', 'Neuquén'                                              ),
    ('Localidad 44', 'Neuquén'                                              ),
    ('Localidad 45', 'Neuquén'                                              ),
    ('Localidad 46', 'Río Negro'                                            ),
    ('Localidad 47', 'Río Negro'                                            ),
    ('Localidad 48', 'Río Negro'                                            ),
    ('Localidad 49', 'Salta'                                                ),
    ('Localidad 50', 'Salta'                                                ),
    ('Localidad 51', 'Salta'                                                ),
    ('Localidad 52', 'San Juan'                                             ),
    ('Localidad 53', 'San Juan'                                             ),
    ('Localidad 54', 'San Juan'                                             ),
    ('Localidad 55', 'San Luis'                                             ),
    ('Localidad 56', 'San Luis'                                             ),
    ('Localidad 57', 'San Luis'                                             ),
    ('Localidad 58', 'Santa Cruz'                                           ),
    ('Localidad 59', 'Santa Cruz'                                           ),
    ('Localidad 60', 'Santa Cruz'                                           ),
    ('Localidad 61', 'Santa Fe'                                             ),
    ('Localidad 62', 'Santa Fe'                                             ),
    ('Localidad 63', 'Santa Fe'                                             ),
    ('Localidad 64', 'Santiago del Estero'                                  ),
    ('Localidad 65', 'Santiago del Estero'                                  ),
    ('Localidad 66', 'Santiago del Estero'                                  ),
    ('Localidad 67', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'),
    ('Localidad 68', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'),
    ('Localidad 69', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'),
    ('Localidad 70', 'Tucumán'                                              ),
    ('Localidad 71', 'Tucumán'                                              ),
    ('Localidad 72', 'Tucumán'                                              );

INSERT INTO persona(cuil, nombre_apellido, domicilio) VALUES
    ('20-10000000-01', 'Juan Perez',        'A'),
    ('20-20000000-02', 'Maria Rodriguez',   'B'),
    ('20-30000000-03', 'Pedro Gomez',       'C'),
    ('20-40000000-04', 'Ana Fernandez',     'D'),
    ('20-50000000-05', 'Lucas Martinez',    'E'),
    ('20-60000000-06', 'Carla Sanchez',     'F'),
    ('20-70000000-07', 'Jose Gonzalez',     'G'),
    ('20-80000000-08', 'Sofia Lopez',       'H'),
    ('20-90000000-09', 'Carlos Diaz',       'I'),
    ('20-10000000-10', 'Florencia Perez',   'J'),
    ('20-11000000-11', 'Martin Rodriguez',  'K'),
    ('20-12000000-12', 'Valentina Gomez',   'L'),
    ('20-13000000-13', 'Agustin Fernandez', 'M');

INSERT INTO chofer(cuil, antiguedad, sueldo) VALUES
    ('20-10000000-01', 5,  20000),
    ('20-20000000-02', 10, 30000),
    ('20-30000000-03', 2,  15000),
    ('20-40000000-04', 1,  10000),
    ('20-50000000-05', 3,  18000),
    ('20-60000000-06', 4,  25000);

INSERT INTO vehiculo(patente, modelo, marca, seguro, tipo) VALUES
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
	(3, 15, TO_DATE('02-05-2022', 'DD-MM-YYYY')),
	(4, 25, TO_DATE('26-04-2023', 'DD-MM-YYYY')),
	(5, 35, TO_DATE('15-05-2023', 'DD-MM-YYYY'));

INSERT INTO paquete(
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

INSERT INTO choque(numero, provincia, fecha, costo, descripcion) VALUES 
	(1, 'Buenos Aires', TO_DATE('01-02-2022', 'DD-MM-YYYY'), 30000, '-'),
	(2, 'Buenos Aires', TO_DATE('02-02-2022', 'DD-MM-YYYY'), 40000, '-'),
	(1, 'San Juan',     TO_DATE('03-03-2022', 'DD-MM-YYYY'), 50000, '-'),
	(1, 'San Luis',     TO_DATE('04-03-2022', 'DD-MM-YYYY'), 60000, '-'),
	(1, 'La Rioja',     TO_DATE('01-01-2023', 'DD-MM-YYYY'), 70000, '-'),
	(1, 'Mendoza',      TO_DATE('23-04-2023', 'DD-MM-YYYY'), 70000, '-'),
	(1, 'Córdoba',      TO_DATE('03-03-2023', 'DD-MM-YYYY'), 70000, '-');

INSERT INTO viaje_choque(numero_choque, provincia_choque, codigo_viaje) VALUES 
    (1, 'Buenos Aires', 1),
    (1, 'San Juan',     2),
    (1, 'Mendoza',      4);

INSERT INTO participo_choque(numero_choque, provincia_choque, patente_vehiculo) VALUES
    (1, 'Buenos Aires', 'DEF456'),
    (2, 'Buenos Aires', 'JKL012'),
    (1, 'San Juan',     'MNO345'),
    (1, 'San Luis',     'REP120'),
    (1, 'La Rioja',     'GHI789'),
    (1, 'Mendoza',      'PQR678'),
    (1, 'Córdoba',      'IOE450');

-- USUARIOS

-- DBA: Debe tener acceso de lectura y escritura a toda la base de datos.
CREATE USER DBA WITH ENCRYPTED PASSWORD '1234';
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA PUBLIC TO DBA;

-- Gerente de la Empresa: Debe tener acceso de lectura a toda la base de datos.
CREATE USER GERENTE WITH ENCRYPTED PASSWORD '12345';
GRANT SELECT ON ALL TABLES IN SCHEMA PUBLIC TO GERENTE;

-- Jefe de Logística
CREATE USER JEFE_LOGISTICA WITH ENCRYPTED PASSWORD '12345678';
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE camiones, chofer, choferes_camiones, viaje, paquete, viaje_recorrio TO JEFE_LOGISTICA;
-- Deben tener acceso de lectura y escritura a todos los datos relativos a los camioneros, camiones y viajes.
-- Esto obviamente incluye las tablas camiones, chofer, choferes_camiones, viaje
-- Pero consideramos que tambien debia tener acceso a las tablas paquete y viaje_recorrio dado que estan muy relacionadas a las otras, ademas de que es justamente el jefe de logistica


-- CONSULTAS

-- CONSULTA PRIORITARIA (tenerla en cuenta para el diseño fisico de la BD)
-- Listado de paquetes (todos sus datos) ordenado por precio.
CREATE VIEW paquetes_ordenados AS (SELECT * FROM paquete ORDER BY valor DESC);

SELECT * FROM paquetes_ordenados;

-- 2. Choferes (todos los datos) que entregaron paquetes en Liniers (Buenos Aires).
SELECT * FROM chofer NATURAL JOIN persona
WHERE EXISTS (
    SELECT * FROM viaje
    WHERE viaje.cuil_chofer=chofer.cuil AND EXISTS (
        SELECT * FROM localidad
        WHERE localidad.nombre = 'Liniers' AND
            localidad.provincia = 'Buenos Aires' AND
            EXISTS (
                SELECT * FROM paquete
                WHERE paquete.codigo_viaje=viaje.numero AND
                    paquete.entrega_localidad_codigo=localidad.codigo
        )
    )
)

-- Otra forma de hacerlo:
SELECT * FROM persona NATURAL JOIN (
    SELECT chofer.* FROM chofer, viaje, localidad, paquete WHERE
        chofer.cuil = viaje.cuil_chofer AND 
        paquete.codigo_viaje = viaje.numero AND
        paquete.entrega_localidad_codigo = localidad.codigo AND
        localidad.nombre = 'Liniers' AND
        localidad.provincia = 'Buenos Aires'
) AS choferes_liniers

-- 3. Choferes (todos los datos) que participaron en accidentes en el año 2022 y también en el 2023.
SELECT * 
FROM chofer NATURAL JOIN persona
WHERE EXISTS (
    SELECT * FROM viaje
    WHERE viaje.cuil_chofer=chofer.cuil AND EXISTS (
        SELECT * FROM viaje_choque
        WHERE viaje_choque.codigo_viaje = viaje.numero AND EXISTS (
            SELECT * FROM choque
            WHERE choque.numero = viaje_choque.numero_choque AND choque.provincia = viaje_choque.provincia_choque AND
                EXTRACT(YEAR FROM choque.fecha) = 2022
        )
    )
) AND EXISTS (
    SELECT * FROM viaje
    WHERE viaje.cuil_chofer=chofer.cuil AND EXISTS (
        SELECT * FROM viaje_choque
        WHERE viaje_choque.codigo_viaje = viaje.numero AND EXISTS (
            SELECT * FROM choque
            WHERE choque.numero = viaje_choque.numero_choque AND choque.provincia = viaje_choque.provincia_choque AND
                EXTRACT(YEAR FROM choque.fecha) = 2023
        )
    )
)

-- 4. Localidades a las que no se hicieron envíos durante 2022.
SELECT * FROM localidad WHERE NOT EXISTS (
    SELECT * FROM paquete WHERE localidad.codigo = paquete.entrega_localidad_codigo AND EXISTS (
        SELECT * FROM viaje WHERE viaje.numero = paquete.codigo_viaje AND EXISTS (
            SELECT * FROM viaje_recorrio WHERE
                viaje_recorrio.codigo_viaje = viaje.numero AND
                viaje_recorrio.codigo_localidad = localidad.codigo AND
                EXTRACT(YEAR FROM viaje_recorrio.fecha_hora) = 2022
        )
    )
);

-- 5. Choferes (todos los datos) que realizaron más viajes.
SELECT * FROM persona NATURAL JOIN (
    SELECT cuil_chofer AS cuil
    FROM viaje
    GROUP BY cuil_chofer
    HAVING COUNT(*) = (
        SELECT COUNT(*) FROM viaje GROUP BY cuil_chofer ORDER BY COUNT(*) DESC LIMIT 1
    )
) AS choferes_mas_viajes;

-- 6. Camiones (todos los datos) que fueron (entregaron paquetes) a todas las localidades de Buenos Aires.
SELECT * FROM camiones WHERE NOT EXISTS (
    SELECT * FROM localidad
    WHERE provincia = 'Buenos Aires' AND NOT EXISTS (
        SELECT * FROM viaje
        WHERE viaje.patente_camion = camiones.patente AND EXISTS (
            SELECT * FROM paquete
            WHERE paquete.codigo_viaje = viaje.numero AND
                paquete.entrega_localidad_codigo = localidad.codigo
        )
    )
)