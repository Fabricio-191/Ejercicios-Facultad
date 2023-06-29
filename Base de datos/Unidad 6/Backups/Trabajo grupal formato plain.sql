--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-06-28 12:11:40

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 5 (class 2615 OID 50154)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 3461 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS '';


--
-- TOC entry 862 (class 1247 OID 50177)
-- Name: cuil; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.cuil AS text
	CONSTRAINT cuil_check CHECK ((VALUE ~ '^[0-9]{2}-[0-9]{1,9}-[0-9]{1,2}$'::text));


ALTER DOMAIN public.cuil OWNER TO postgres;

--
-- TOC entry 855 (class 1247 OID 50164)
-- Name: orientacion; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.orientacion AS ENUM (
    'N',
    'S',
    'E',
    'O'
);


ALTER TYPE public.orientacion OWNER TO postgres;

--
-- TOC entry 858 (class 1247 OID 50174)
-- Name: patente; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.patente AS text
	CONSTRAINT patente_check CHECK (((VALUE ~ '^[A-Z]{3}[0-9]{3}$'::text) OR (VALUE ~ '^[A-Z]{2}[0-9]{3}[A-Z]{2}$'::text)));


ALTER DOMAIN public.patente OWNER TO postgres;

--
-- TOC entry 852 (class 1247 OID 50157)
-- Name: tipo_vehiculo; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.tipo_vehiculo AS ENUM (
    'Camion',
    'Auto',
    'Moto'
);


ALTER TYPE public.tipo_vehiculo OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 50186)
-- Name: camiones; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.camiones (
    patente public.patente NOT NULL,
    valor integer NOT NULL,
    kilometraje integer NOT NULL,
    CONSTRAINT camiones_kilometraje_check CHECK ((kilometraje >= 0)),
    CONSTRAINT camiones_valor_check CHECK ((valor >= 0))
);


ALTER TABLE public.camiones OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 50207)
-- Name: choferes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.choferes (
    cuil public.cuil NOT NULL,
    antiguedad integer NOT NULL,
    sueldo real NOT NULL,
    CONSTRAINT choferes_antiguedad_check CHECK ((antiguedad >= 0)),
    CONSTRAINT choferes_sueldo_check CHECK ((sueldo >= (0)::double precision))
);


ALTER TABLE public.choferes OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 50216)
-- Name: choferes_camiones; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.choferes_camiones (
    cuil public.cuil NOT NULL,
    patente text NOT NULL
);


ALTER TABLE public.choferes_camiones OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 50320)
-- Name: choques; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.choques (
    numero integer NOT NULL,
    provincia text NOT NULL,
    fecha date NOT NULL,
    costo real NOT NULL,
    descripcion text NOT NULL,
    CONSTRAINT choques_costo_check CHECK ((costo > (0)::double precision)),
    CONSTRAINT choques_fecha_check CHECK ((fecha < CURRENT_DATE))
);


ALTER TABLE public.choques OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 50241)
-- Name: localidades; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.localidades (
    codigo integer NOT NULL,
    nombre text NOT NULL,
    provincia text NOT NULL
);


ALTER TABLE public.localidades OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 50240)
-- Name: localidades_codigo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.localidades_codigo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.localidades_codigo_seq OWNER TO postgres;

--
-- TOC entry 3468 (class 0 OID 0)
-- Dependencies: 220
-- Name: localidades_codigo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.localidades_codigo_seq OWNED BY public.localidades.codigo;


--
-- TOC entry 225 (class 1259 OID 50295)
-- Name: paquetes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.paquetes (
    numero integer NOT NULL,
    codigo_viaje integer NOT NULL,
    valor real NOT NULL,
    precio_translado real NOT NULL,
    destinatario_cuil public.cuil NOT NULL,
    remitente_cuil public.cuil NOT NULL,
    entrega_localidad_codigo integer NOT NULL,
    entrega_direccion_calle text NOT NULL,
    entrega_direccion_orientacion public.orientacion NOT NULL,
    entrega_direccion_numero integer NOT NULL,
    CONSTRAINT paquetes_precio_translado_check CHECK ((precio_translado > (0)::double precision)),
    CONSTRAINT paquetes_valor_check CHECK ((valor > (0)::double precision))
);


ALTER TABLE public.paquetes OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 50294)
-- Name: paquetes_numero_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.paquetes_numero_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.paquetes_numero_seq OWNER TO postgres;

--
-- TOC entry 3470 (class 0 OID 0)
-- Dependencies: 224
-- Name: paquetes_numero_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.paquetes_numero_seq OWNED BY public.paquetes.numero;


--
-- TOC entry 229 (class 1259 OID 50381)
-- Name: paquetes_ordenados; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.paquetes_ordenados AS
 SELECT paquetes.numero,
    paquetes.codigo_viaje,
    paquetes.valor,
    paquetes.precio_translado,
    paquetes.destinatario_cuil,
    paquetes.remitente_cuil,
    paquetes.entrega_localidad_codigo,
    paquetes.entrega_direccion_calle,
    paquetes.entrega_direccion_orientacion,
    paquetes.entrega_direccion_numero
   FROM public.paquetes
  ORDER BY paquetes.valor DESC;


ALTER TABLE public.paquetes_ordenados OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 50334)
-- Name: participo_choque; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.participo_choque (
    numero_choque integer NOT NULL,
    provincia_choque text NOT NULL,
    patente_vehiculo public.patente NOT NULL
);


ALTER TABLE public.participo_choque OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 50200)
-- Name: personas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.personas (
    cuil public.cuil NOT NULL,
    nombre_apellido text NOT NULL,
    domicilio text NOT NULL
);


ALTER TABLE public.personas OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 50233)
-- Name: provincias; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.provincias (
    nombre text NOT NULL
);


ALTER TABLE public.provincias OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 50179)
-- Name: vehiculos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vehiculos (
    patente public.patente NOT NULL,
    modelo text NOT NULL,
    marca text NOT NULL,
    seguro text NOT NULL,
    tipo public.tipo_vehiculo NOT NULL
);


ALTER TABLE public.vehiculos OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 50254)
-- Name: viaje; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.viaje (
    numero integer NOT NULL,
    patente_camion text NOT NULL,
    cuil_chofer public.cuil NOT NULL,
    kilometros real NOT NULL,
    fecha_inicio date NOT NULL,
    fecha_fin date NOT NULL,
    CONSTRAINT viaje_check CHECK ((fecha_inicio < fecha_fin)),
    CONSTRAINT viaje_kilometros_check CHECK ((kilometros > (0)::double precision))
);


ALTER TABLE public.viaje OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 50356)
-- Name: viaje_choque; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.viaje_choque (
    numero_choque integer NOT NULL,
    provincia_choque text NOT NULL,
    codigo_viaje integer NOT NULL
);


ALTER TABLE public.viaje_choque OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 50278)
-- Name: viaje_recorrio; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.viaje_recorrio (
    codigo_viaje integer NOT NULL,
    codigo_localidad integer NOT NULL,
    fecha_hora timestamp without time zone NOT NULL,
    CONSTRAINT viaje_recorrio_fecha_hora_check CHECK ((fecha_hora < CURRENT_TIMESTAMP))
);


ALTER TABLE public.viaje_recorrio OWNER TO postgres;

--
-- TOC entry 3240 (class 2604 OID 50244)
-- Name: localidades codigo; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.localidades ALTER COLUMN codigo SET DEFAULT nextval('public.localidades_codigo_seq'::regclass);


--
-- TOC entry 3241 (class 2604 OID 50298)
-- Name: paquetes numero; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paquetes ALTER COLUMN numero SET DEFAULT nextval('public.paquetes_numero_seq'::regclass);


--
-- TOC entry 3442 (class 0 OID 50186)
-- Dependencies: 215
-- Data for Name: camiones; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.camiones (patente, valor, kilometraje) FROM stdin;
DEF456	75000	80000
JKL012	90000	120000
MNO345	50000	50000
PQR678	100000	100000
STU901	150000	150000
VWX234	200000	200000
\.


--
-- TOC entry 3444 (class 0 OID 50207)
-- Dependencies: 217
-- Data for Name: choferes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.choferes (cuil, antiguedad, sueldo) FROM stdin;
20-10000000-01	5	20000
20-20000000-02	10	30000
20-30000000-03	2	15000
20-40000000-04	1	10000
20-50000000-05	3	18000
20-60000000-06	4	25000
\.


--
-- TOC entry 3445 (class 0 OID 50216)
-- Dependencies: 218
-- Data for Name: choferes_camiones; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.choferes_camiones (cuil, patente) FROM stdin;
20-10000000-01	DEF456
20-20000000-02	MNO345
20-30000000-03	JKL012
20-40000000-04	VWX234
20-50000000-05	PQR678
\.


--
-- TOC entry 3453 (class 0 OID 50320)
-- Dependencies: 226
-- Data for Name: choques; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.choques (numero, provincia, fecha, costo, descripcion) FROM stdin;
1	Buenos Aires	2022-02-01	30000	-
2	Buenos Aires	2022-02-02	40000	-
1	San Juan	2022-03-03	50000	-
1	San Luis	2022-03-04	60000	-
1	La Rioja	2023-01-01	70000	-
1	Mendoza	2023-04-23	70000	-
1	Córdoba	2023-03-03	70000	-
\.


--
-- TOC entry 3448 (class 0 OID 50241)
-- Dependencies: 221
-- Data for Name: localidades; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.localidades (codigo, nombre, provincia) FROM stdin;
1	localidades 1	Buenos Aires
2	Liniers	Buenos Aires
3	localidades 3	Buenos Aires
4	localidades 4	Ciudad Autónoma de Buenos Aires
5	localidades 5	Ciudad Autónoma de Buenos Aires
6	localidades 6	Ciudad Autónoma de Buenos Aires
7	localidades 7	Catamarca
8	localidades 8	Catamarca
9	localidades 9	Catamarca
10	localidades 10	Chaco
11	localidades 11	Chaco
12	localidades 12	Chaco
13	localidades 13	Chubut
14	localidades 14	Chubut
15	localidades 15	Chubut
16	localidades 16	Córdoba
17	localidades 17	Córdoba
18	localidades 18	Córdoba
19	localidades 19	Corrientes
20	localidades 20	Corrientes
21	localidades 21	Corrientes
22	localidades 22	Entre Ríos
23	localidades 23	Entre Ríos
24	localidades 24	Entre Ríos
25	localidades 25	Formosa
26	localidades 26	Formosa
27	localidades 27	Formosa
28	localidades 28	Jujuy
29	localidades 29	Jujuy
30	localidades 30	Jujuy
31	localidades 31	La Pampa
32	localidades 32	La Pampa
33	localidades 33	La Pampa
34	localidades 34	La Rioja
35	localidades 35	La Rioja
36	localidades 36	La Rioja
37	localidades 37	Mendoza
38	localidades 38	Mendoza
39	localidades 39	Mendoza
40	localidades 40	Misiones
41	localidades 41	Misiones
42	localidades 42	Misiones
43	localidades 43	Neuquén
44	localidades 44	Neuquén
45	localidades 45	Neuquén
46	localidades 46	Río Negro
47	localidades 47	Río Negro
48	localidades 48	Río Negro
49	localidades 49	Salta
50	localidades 50	Salta
51	localidades 51	Salta
52	localidades 52	San Juan
53	localidades 53	San Juan
54	localidades 54	San Juan
55	localidades 55	San Luis
56	localidades 56	San Luis
57	localidades 57	San Luis
58	localidades 58	Santa Cruz
59	localidades 59	Santa Cruz
60	localidades 60	Santa Cruz
61	localidades 61	Santa Fe
62	localidades 62	Santa Fe
63	localidades 63	Santa Fe
64	localidades 64	Santiago del Estero
65	localidades 65	Santiago del Estero
66	localidades 66	Santiago del Estero
67	localidades 67	Tierra del Fuego, Antártida e Islas del Atlántico Sur
68	localidades 68	Tierra del Fuego, Antártida e Islas del Atlántico Sur
69	localidades 69	Tierra del Fuego, Antártida e Islas del Atlántico Sur
70	localidades 70	Tucumán
71	localidades 71	Tucumán
72	localidades 72	Tucumán
\.


--
-- TOC entry 3452 (class 0 OID 50295)
-- Dependencies: 225
-- Data for Name: paquetes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.paquetes (numero, codigo_viaje, valor, precio_translado, destinatario_cuil, remitente_cuil, entrega_localidad_codigo, entrega_direccion_calle, entrega_direccion_orientacion, entrega_direccion_numero) FROM stdin;
1	1	3000	5000	20-30000000-01	20-30000000-03	1	Calle a	E	3000
2	1	500000	10000	20-10000000-01	20-40000000-04	2	Calle b	N	600
3	1	2000	2000	20-80000000-08	20-90000000-09	3	Calle c	S	100
4	1	20000	3000	20-70000000-07	20-80000000-08	4	Calle d	O	200
5	2	4000	4000	20-90000000-09	20-10000000-10	5	Calle e	N	300
6	2	5000	4000	20-10000000-10	20-11000000-11	6	Calle f	S	300
7	3	10000	4000	20-11000000-11	20-12000000-12	15	Calle g	O	400
8	4	50000	4000	20-12000000-12	20-13000000-13	25	Calle h	S	500
9	5	3000	4000	20-13000000-13	20-11000000-11	35	Calle i	N	600
\.


--
-- TOC entry 3454 (class 0 OID 50334)
-- Dependencies: 227
-- Data for Name: participo_choque; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.participo_choque (numero_choque, provincia_choque, patente_vehiculo) FROM stdin;
1	Buenos Aires	DEF456
2	Buenos Aires	JKL012
1	San Juan	MNO345
1	San Luis	REP120
1	La Rioja	GHI789
1	Mendoza	PQR678
1	Córdoba	IOE450
\.


--
-- TOC entry 3443 (class 0 OID 50200)
-- Dependencies: 216
-- Data for Name: personas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.personas (cuil, nombre_apellido, domicilio) FROM stdin;
20-10000000-01	Juan Perez	A
20-20000000-02	Maria Rodriguez	B
20-30000000-03	Pedro Gomez	C
20-40000000-04	Ana Fernandez	D
20-50000000-05	Lucas Martinez	E
20-60000000-06	Carla Sanchez	F
20-70000000-07	Jose Gonzalez	G
20-80000000-08	Sofia Lopez	H
20-90000000-09	Carlos Diaz	I
20-10000000-10	Florencia Perez	J
20-11000000-11	Martin Rodriguez	K
20-12000000-12	Valentina Gomez	L
20-13000000-13	Agustin Fernandez	M
\.


--
-- TOC entry 3446 (class 0 OID 50233)
-- Dependencies: 219
-- Data for Name: provincias; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.provincias (nombre) FROM stdin;
Buenos Aires
Ciudad Autónoma de Buenos Aires
Catamarca
Chaco
Chubut
Córdoba
Corrientes
Entre Ríos
Formosa
Jujuy
La Pampa
La Rioja
Mendoza
Misiones
Neuquén
Río Negro
Salta
San Juan
San Luis
Santa Cruz
Santa Fe
Santiago del Estero
Tierra del Fuego, Antártida e Islas del Atlántico Sur
Tucumán
\.


--
-- TOC entry 3441 (class 0 OID 50179)
-- Dependencies: 214
-- Data for Name: vehiculos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vehiculos (patente, modelo, marca, seguro, tipo) FROM stdin;
ABC123	Fiesta	Ford	Allianz	Auto
DEF456	Sprinter	Mercedes-Benz	Mapfre	Camion
JKL012	Hilux	Toyota	La Caja	Camion
LPQ310	Tornado	Chevrolet	Sancor	Camion
REP120	Tornado	Chevrolet	Sancor	Camion
MIL210	Tornado	Chevrolet	Sancor	Camion
PQR678	FZ16	Yamaha	Provincia	Camion
STU901	Corolla	Toyota	La Segunda	Camion
VWX234	CBR1000	Honda	Allianz	Camion
QPR310	CBR1000	Honda	Allianz	Camion
GHI789	CBR600	Honda	Sancor	Moto
MLO456	Civic	Honda	La Segunda	Auto
MNO345	Constellation	Volkswagen	Mapfre	Camion
IOE450	R1	Yamaha	Provincia	Moto
\.


--
-- TOC entry 3449 (class 0 OID 50254)
-- Dependencies: 222
-- Data for Name: viaje; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.viaje (numero, patente_camion, cuil_chofer, kilometros, fecha_inicio, fecha_fin) FROM stdin;
1	DEF456	20-10000000-01	1000	2022-01-01	2022-02-05
2	MNO345	20-20000000-02	4000	2022-02-02	2022-03-30
3	VWX234	20-40000000-04	3000	2022-03-15	2022-08-02
4	DEF456	20-10000000-01	2000	2023-04-20	2023-05-04
5	MNO345	20-20000000-02	5000	2023-05-01	2023-06-13
\.


--
-- TOC entry 3455 (class 0 OID 50356)
-- Dependencies: 228
-- Data for Name: viaje_choque; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.viaje_choque (numero_choque, provincia_choque, codigo_viaje) FROM stdin;
1	Buenos Aires	1
1	San Juan	2
1	Mendoza	4
\.


--
-- TOC entry 3450 (class 0 OID 50278)
-- Dependencies: 223
-- Data for Name: viaje_recorrio; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.viaje_recorrio (codigo_viaje, codigo_localidad, fecha_hora) FROM stdin;
1	1	2022-01-08 00:00:00
1	2	2022-01-12 00:00:00
1	3	2022-01-16 00:00:00
1	4	2022-01-21 00:00:00
2	5	2022-02-14 00:00:00
2	6	2022-03-18 00:00:00
3	15	2022-05-02 00:00:00
4	25	2023-04-26 00:00:00
5	35	2023-05-15 00:00:00
\.


--
-- TOC entry 3478 (class 0 OID 0)
-- Dependencies: 220
-- Name: localidades_codigo_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.localidades_codigo_seq', 72, true);


--
-- TOC entry 3479 (class 0 OID 0)
-- Dependencies: 224
-- Name: paquetes_numero_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.paquetes_numero_seq', 9, true);


--
-- TOC entry 3256 (class 2606 OID 50194)
-- Name: camiones camiones_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.camiones
    ADD CONSTRAINT camiones_pkey PRIMARY KEY (patente);


--
-- TOC entry 3262 (class 2606 OID 50222)
-- Name: choferes_camiones choferes_camiones_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.choferes_camiones
    ADD CONSTRAINT choferes_camiones_pkey PRIMARY KEY (cuil, patente);


--
-- TOC entry 3260 (class 2606 OID 50215)
-- Name: choferes choferes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.choferes
    ADD CONSTRAINT choferes_pkey PRIMARY KEY (cuil);


--
-- TOC entry 3274 (class 2606 OID 50328)
-- Name: choques choques_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.choques
    ADD CONSTRAINT choques_pkey PRIMARY KEY (numero, provincia);


--
-- TOC entry 3266 (class 2606 OID 50248)
-- Name: localidades localidades_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.localidades
    ADD CONSTRAINT localidades_pkey PRIMARY KEY (codigo);


--
-- TOC entry 3272 (class 2606 OID 50304)
-- Name: paquetes paquetes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paquetes
    ADD CONSTRAINT paquetes_pkey PRIMARY KEY (numero);


--
-- TOC entry 3276 (class 2606 OID 50340)
-- Name: participo_choque participo_choque_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.participo_choque
    ADD CONSTRAINT participo_choque_pkey PRIMARY KEY (numero_choque, provincia_choque, patente_vehiculo);


--
-- TOC entry 3258 (class 2606 OID 50206)
-- Name: personas personas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.personas
    ADD CONSTRAINT personas_pkey PRIMARY KEY (cuil);


--
-- TOC entry 3264 (class 2606 OID 50239)
-- Name: provincias provincias_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.provincias
    ADD CONSTRAINT provincias_pkey PRIMARY KEY (nombre);


--
-- TOC entry 3254 (class 2606 OID 50185)
-- Name: vehiculos vehiculos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehiculos
    ADD CONSTRAINT vehiculos_pkey PRIMARY KEY (patente);


--
-- TOC entry 3278 (class 2606 OID 50362)
-- Name: viaje_choque viaje_choque_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viaje_choque
    ADD CONSTRAINT viaje_choque_pkey PRIMARY KEY (numero_choque, provincia_choque, codigo_viaje);


--
-- TOC entry 3268 (class 2606 OID 50262)
-- Name: viaje viaje_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viaje
    ADD CONSTRAINT viaje_pkey PRIMARY KEY (numero);


--
-- TOC entry 3270 (class 2606 OID 50283)
-- Name: viaje_recorrio viaje_recorrio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viaje_recorrio
    ADD CONSTRAINT viaje_recorrio_pkey PRIMARY KEY (codigo_localidad, codigo_viaje, fecha_hora);


--
-- TOC entry 3279 (class 2606 OID 50195)
-- Name: camiones camiones_patente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.camiones
    ADD CONSTRAINT camiones_patente_fkey FOREIGN KEY (patente) REFERENCES public.vehiculos(patente) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3280 (class 2606 OID 50223)
-- Name: choferes_camiones choferes_camiones_cuil_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.choferes_camiones
    ADD CONSTRAINT choferes_camiones_cuil_fkey FOREIGN KEY (cuil) REFERENCES public.choferes(cuil) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3281 (class 2606 OID 50228)
-- Name: choferes_camiones choferes_camiones_patente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.choferes_camiones
    ADD CONSTRAINT choferes_camiones_patente_fkey FOREIGN KEY (patente) REFERENCES public.camiones(patente) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3291 (class 2606 OID 50329)
-- Name: choques choques_provincia_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.choques
    ADD CONSTRAINT choques_provincia_fkey FOREIGN KEY (provincia) REFERENCES public.provincias(nombre) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3282 (class 2606 OID 50249)
-- Name: localidades localidades_provincia_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.localidades
    ADD CONSTRAINT localidades_provincia_fkey FOREIGN KEY (provincia) REFERENCES public.provincias(nombre) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3288 (class 2606 OID 50305)
-- Name: paquetes paquetes_codigo_viaje_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paquetes
    ADD CONSTRAINT paquetes_codigo_viaje_fkey FOREIGN KEY (codigo_viaje) REFERENCES public.viaje(numero) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3289 (class 2606 OID 50315)
-- Name: paquetes paquetes_entrega_localidad_codigo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paquetes
    ADD CONSTRAINT paquetes_entrega_localidad_codigo_fkey FOREIGN KEY (entrega_localidad_codigo) REFERENCES public.localidades(codigo) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3290 (class 2606 OID 50310)
-- Name: paquetes paquetes_remitente_cuil_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paquetes
    ADD CONSTRAINT paquetes_remitente_cuil_fkey FOREIGN KEY (remitente_cuil) REFERENCES public.personas(cuil) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3292 (class 2606 OID 50351)
-- Name: participo_choque participo_choque_numero_choque_provincia_choque_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.participo_choque
    ADD CONSTRAINT participo_choque_numero_choque_provincia_choque_fkey FOREIGN KEY (numero_choque, provincia_choque) REFERENCES public.choques(numero, provincia) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3293 (class 2606 OID 50346)
-- Name: participo_choque participo_choque_patente_vehiculo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.participo_choque
    ADD CONSTRAINT participo_choque_patente_vehiculo_fkey FOREIGN KEY (patente_vehiculo) REFERENCES public.vehiculos(patente) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3294 (class 2606 OID 50341)
-- Name: participo_choque participo_choque_provincia_choque_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.participo_choque
    ADD CONSTRAINT participo_choque_provincia_choque_fkey FOREIGN KEY (provincia_choque) REFERENCES public.provincias(nombre) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3295 (class 2606 OID 50368)
-- Name: viaje_choque viaje_choque_codigo_viaje_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viaje_choque
    ADD CONSTRAINT viaje_choque_codigo_viaje_fkey FOREIGN KEY (codigo_viaje) REFERENCES public.viaje(numero) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3296 (class 2606 OID 50373)
-- Name: viaje_choque viaje_choque_numero_choque_provincia_choque_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viaje_choque
    ADD CONSTRAINT viaje_choque_numero_choque_provincia_choque_fkey FOREIGN KEY (numero_choque, provincia_choque) REFERENCES public.choques(numero, provincia) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3297 (class 2606 OID 50363)
-- Name: viaje_choque viaje_choque_provincia_choque_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viaje_choque
    ADD CONSTRAINT viaje_choque_provincia_choque_fkey FOREIGN KEY (provincia_choque) REFERENCES public.provincias(nombre) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3283 (class 2606 OID 50268)
-- Name: viaje viaje_cuil_chofer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viaje
    ADD CONSTRAINT viaje_cuil_chofer_fkey FOREIGN KEY (cuil_chofer) REFERENCES public.choferes(cuil) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3284 (class 2606 OID 50273)
-- Name: viaje viaje_patente_camion_cuil_chofer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viaje
    ADD CONSTRAINT viaje_patente_camion_cuil_chofer_fkey FOREIGN KEY (patente_camion, cuil_chofer) REFERENCES public.choferes_camiones(patente, cuil) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3285 (class 2606 OID 50263)
-- Name: viaje viaje_patente_camion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viaje
    ADD CONSTRAINT viaje_patente_camion_fkey FOREIGN KEY (patente_camion) REFERENCES public.camiones(patente) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3286 (class 2606 OID 50289)
-- Name: viaje_recorrio viaje_recorrio_codigo_localidad_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viaje_recorrio
    ADD CONSTRAINT viaje_recorrio_codigo_localidad_fkey FOREIGN KEY (codigo_localidad) REFERENCES public.localidades(codigo);


--
-- TOC entry 3287 (class 2606 OID 50284)
-- Name: viaje_recorrio viaje_recorrio_codigo_viaje_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viaje_recorrio
    ADD CONSTRAINT viaje_recorrio_codigo_viaje_fkey FOREIGN KEY (codigo_viaje) REFERENCES public.viaje(numero);


--
-- TOC entry 3462 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;


--
-- TOC entry 3463 (class 0 OID 0)
-- Dependencies: 215
-- Name: TABLE camiones; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.camiones TO dba;
GRANT SELECT ON TABLE public.camiones TO gerente;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.camiones TO jefe_logistica;


--
-- TOC entry 3464 (class 0 OID 0)
-- Dependencies: 217
-- Name: TABLE choferes; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.choferes TO dba;
GRANT SELECT ON TABLE public.choferes TO gerente;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.choferes TO jefe_logistica;


--
-- TOC entry 3465 (class 0 OID 0)
-- Dependencies: 218
-- Name: TABLE choferes_camiones; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.choferes_camiones TO dba;
GRANT SELECT ON TABLE public.choferes_camiones TO gerente;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.choferes_camiones TO jefe_logistica;


--
-- TOC entry 3466 (class 0 OID 0)
-- Dependencies: 226
-- Name: TABLE choques; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.choques TO dba;
GRANT SELECT ON TABLE public.choques TO gerente;


--
-- TOC entry 3467 (class 0 OID 0)
-- Dependencies: 221
-- Name: TABLE localidades; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.localidades TO dba;
GRANT SELECT ON TABLE public.localidades TO gerente;


--
-- TOC entry 3469 (class 0 OID 0)
-- Dependencies: 225
-- Name: TABLE paquetes; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.paquetes TO dba;
GRANT SELECT ON TABLE public.paquetes TO gerente;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.paquetes TO jefe_logistica;


--
-- TOC entry 3471 (class 0 OID 0)
-- Dependencies: 227
-- Name: TABLE participo_choque; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.participo_choque TO dba;
GRANT SELECT ON TABLE public.participo_choque TO gerente;


--
-- TOC entry 3472 (class 0 OID 0)
-- Dependencies: 216
-- Name: TABLE personas; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.personas TO dba;
GRANT SELECT ON TABLE public.personas TO gerente;


--
-- TOC entry 3473 (class 0 OID 0)
-- Dependencies: 219
-- Name: TABLE provincias; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.provincias TO dba;
GRANT SELECT ON TABLE public.provincias TO gerente;


--
-- TOC entry 3474 (class 0 OID 0)
-- Dependencies: 214
-- Name: TABLE vehiculos; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.vehiculos TO dba;
GRANT SELECT ON TABLE public.vehiculos TO gerente;


--
-- TOC entry 3475 (class 0 OID 0)
-- Dependencies: 222
-- Name: TABLE viaje; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.viaje TO dba;
GRANT SELECT ON TABLE public.viaje TO gerente;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.viaje TO jefe_logistica;


--
-- TOC entry 3476 (class 0 OID 0)
-- Dependencies: 228
-- Name: TABLE viaje_choque; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.viaje_choque TO dba;
GRANT SELECT ON TABLE public.viaje_choque TO gerente;


--
-- TOC entry 3477 (class 0 OID 0)
-- Dependencies: 223
-- Name: TABLE viaje_recorrio; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.viaje_recorrio TO dba;
GRANT SELECT ON TABLE public.viaje_recorrio TO gerente;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.viaje_recorrio TO jefe_logistica;


-- Completed on 2023-06-28 12:11:40

--
-- PostgreSQL database dump complete
--

