--
-- PostgreSQL database dump
--

-- Dumped from database version 10.21 (Ubuntu 10.21-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.21 (Ubuntu 10.21-0ubuntu0.18.04.1)

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
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO vagrant;

--
-- Name: castinglist; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.castinglist (
    id integer NOT NULL,
    name character varying(120) NOT NULL,
    age integer,
    gender character varying(120)
);


ALTER TABLE public.castinglist OWNER TO vagrant;

--
-- Name: castinglist_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.castinglist_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.castinglist_id_seq OWNER TO vagrant;

--
-- Name: castinglist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.castinglist_id_seq OWNED BY public.castinglist.id;


--
-- Name: collections; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.collections (
    id integer NOT NULL,
    movie_id integer,
    casting_id integer
);


ALTER TABLE public.collections OWNER TO vagrant;

--
-- Name: collections_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.collections_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.collections_id_seq OWNER TO vagrant;

--
-- Name: collections_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.collections_id_seq OWNED BY public.collections.id;


--
-- Name: movielist; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.movielist (
    id integer NOT NULL,
    title character varying(120) NOT NULL,
    release_date timestamp without time zone
);


ALTER TABLE public.movielist OWNER TO vagrant;

--
-- Name: movielist_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.movielist_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movielist_id_seq OWNER TO vagrant;

--
-- Name: movielist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.movielist_id_seq OWNED BY public.movielist.id;


--
-- Name: castinglist id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.castinglist ALTER COLUMN id SET DEFAULT nextval('public.castinglist_id_seq'::regclass);


--
-- Name: collections id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.collections ALTER COLUMN id SET DEFAULT nextval('public.collections_id_seq'::regclass);


--
-- Name: movielist id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.movielist ALTER COLUMN id SET DEFAULT nextval('public.movielist_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.alembic_version (version_num) FROM stdin;
1306e5201255
\.


--
-- Data for Name: castinglist; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.castinglist (id, name, age, gender) FROM stdin;
1	Logan Marshall-Green	45	Male
2	Gal Gadot	37	Female
3	Christ Pine	41	Male
4	Sandra Oh	50	Female
5	Liam Nelson	69	Male
6	Monica Bellucci	58	Female
7	Guy Pearce	55	Male
8	Aidan Quinn	63	Male
9	Laurence Fishburne	61	Male
10	Tom Hanks	66	Male
11	Caleb Landry Jones	32	Male
12	Simu Liu	33	Male
13	Tony Leung	59	Male
14	Awkwafina	34	Female
15	Michael Keaton	70	Male
16	Stanley Tucci	61	Male
17	Amy Ryan	54	Female
18	Colin Firth	61	Male
19	Jude Law	49	Male
20	Laura Linney	58	Female
21	Nicoel Kidman	54	Female
22	Venessa Kirby	34	Female
23	Dwayne Johnson	50	Male
24	Rosamund Pike	43	Female
25	Peter Dinklage	52	Male
26	Eiza González	32	Female
27	Dianne Wiest	74	Female
28	Jessica Chastain	45	Female
29	Lupita Nyongo	39	Female
31	Penelope Cruz	48	Female
32	Diane Kruger	45	Female
33	Bingbing Fan	40	Female
34	John Travolta	68	Male
35	Kelly Preston	57	Female
36	Stacy Keach	81	Male
41	Tom Cruise	59	Male
42	Keenu Reeves	54	Male
\.


--
-- Data for Name: collections; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.collections (id, movie_id, casting_id) FROM stdin;
1	1	1
3	15	2
4	15	3
5	7	4
6	8	5
7	6	5
8	6	6
9	6	7
10	8	8
11	5	5
12	5	9
13	9	10
14	9	11
15	11	12
16	11	13
17	11	14
18	2	34
19	2	35
20	2	36
21	3	28
22	3	29
23	3	31
24	3	27
25	3	33
26	4	16
27	4	18
28	10	23
29	10	2
30	12	17
31	12	15
32	12	16
33	13	24
34	13	25
35	13	27
36	13	32
37	14	22
38	14	19
39	14	7
40	14	21
41	14	18
42	14	20
\.


--
-- Data for Name: movielist; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.movielist (id, title, release_date) FROM stdin;
1	Upgrade	2018-08-28 00:00:00
2	Gotti	2018-09-25 00:00:00
3	The 355	2022-01-07 00:00:00
4	Supernova	2020-08-22 00:00:00
5	The Ice Road	2021-06-25 00:00:00
6	Memory	2022-04-29 00:00:00
7	Umma	2022-03-18 00:00:00
8	Blacklight	2022-05-03 00:00:00
9	Finch	2021-11-05 00:00:00
10	Red Notice	2021-11-12 00:00:00
11	Shang-Chi and the Legend of the Ten Rings	2021-09-03 00:00:00
12	Worth	2021-09-03 00:00:00
13	I Care A Lot	2021-02-19 00:00:00
14	Genius	2016-06-17 00:00:00
15	Wonder Woman	2014-06-29 00:00:00
17	Top Gun: Maverick	2022-05-27 00:00:00
\.


--
-- Name: castinglist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.castinglist_id_seq', 42, true);


--
-- Name: collections_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.collections_id_seq', 42, true);


--
-- Name: movielist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.movielist_id_seq', 17, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: castinglist castinglist_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.castinglist
    ADD CONSTRAINT castinglist_pkey PRIMARY KEY (id);


--
-- Name: collections collections_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.collections
    ADD CONSTRAINT collections_pkey PRIMARY KEY (id);


--
-- Name: movielist movielist_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.movielist
    ADD CONSTRAINT movielist_pkey PRIMARY KEY (id);


--
-- Name: collections collections_casting_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.collections
    ADD CONSTRAINT collections_casting_id_fkey FOREIGN KEY (casting_id) REFERENCES public.castinglist(id);


--
-- Name: collections collections_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.collections
    ADD CONSTRAINT collections_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movielist(id);


--
-- PostgreSQL database dump complete
--

