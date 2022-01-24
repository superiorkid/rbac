--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: superiorkid
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO superiorkid;

--
-- Name: role; Type: TABLE; Schema: public; Owner: superiorkid
--

CREATE TABLE public.role (
    id integer NOT NULL,
    name character varying(64),
    "default" boolean,
    permissions integer
);


ALTER TABLE public.role OWNER TO superiorkid;

--
-- Name: role_id_seq; Type: SEQUENCE; Schema: public; Owner: superiorkid
--

CREATE SEQUENCE public.role_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.role_id_seq OWNER TO superiorkid;

--
-- Name: role_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: superiorkid
--

ALTER SEQUENCE public.role_id_seq OWNED BY public.role.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: superiorkid
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(64),
    email character varying(64),
    password_hash character varying(128),
    role_id integer,
    name character varying(64),
    location character varying(64),
    about_me text,
    member_since timestamp without time zone,
    last_seen timestamp without time zone
);


ALTER TABLE public."user" OWNER TO superiorkid;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: superiorkid
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO superiorkid;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: superiorkid
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: role id; Type: DEFAULT; Schema: public; Owner: superiorkid
--

ALTER TABLE ONLY public.role ALTER COLUMN id SET DEFAULT nextval('public.role_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: superiorkid
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: superiorkid
--

COPY public.alembic_version (version_num) FROM stdin;
dc8d261c6b0b
\.


--
-- Data for Name: role; Type: TABLE DATA; Schema: public; Owner: superiorkid
--

COPY public.role (id, name, "default", permissions) FROM stdin;
1	User	t	7
8	Moderator	f	15
9	Administrator	f	255
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: superiorkid
--

COPY public."user" (id, username, email, password_hash, role_id, name, location, about_me, member_since, last_seen) FROM stdin;
36	susan	susan@example.com	pbkdf2:sha256:260000$CX5uoeTtOcu4nFQY$df61458fc863b214460ec0d9295c69e7d6baa7912c5d212f16dfc9d1382fd555	8	Susan chandra kirana	Selong	Indomie + nasi. best partner	2022-01-23 13:55:14.524094	2022-01-23 15:02:21.513882
34	admin	admin@example.com	pbkdf2:sha256:260000$FYkSfyMUJv7JqZJp$152806a9feaa8a7f9fbbeee661d5875adfe426bf2d540739be09bc60aea1f6fe	9	Moh. Ilhamuddin	Penye Barat	full stack web developer :"	\N	2022-01-23 15:03:27.715091
35	john	john@example.com	pbkdf2:sha256:260000$V1k9UtMP1RPKRM5N$fbe48638f40aa8aab89636ee8ef78c3135c456c6a41e41262cd6bebb80702a35	1	John Jhin Jhun	Sakra	Gamer and tech :? yaps	\N	2022-01-23 15:03:54.725946
\.


--
-- Name: role_id_seq; Type: SEQUENCE SET; Schema: public; Owner: superiorkid
--

SELECT pg_catalog.setval('public.role_id_seq', 9, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: superiorkid
--

SELECT pg_catalog.setval('public.user_id_seq', 36, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: superiorkid
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: role role_name_key; Type: CONSTRAINT; Schema: public; Owner: superiorkid
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_name_key UNIQUE (name);


--
-- Name: role role_pkey; Type: CONSTRAINT; Schema: public; Owner: superiorkid
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: superiorkid
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: ix_role_default; Type: INDEX; Schema: public; Owner: superiorkid
--

CREATE INDEX ix_role_default ON public.role USING btree ("default");


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: superiorkid
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: ix_user_username; Type: INDEX; Schema: public; Owner: superiorkid
--

CREATE UNIQUE INDEX ix_user_username ON public."user" USING btree (username);


--
-- Name: user user_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: superiorkid
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.role(id);


--
-- PostgreSQL database dump complete
--

