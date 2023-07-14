CREATE DATABASE parser_employers;
CREATE TABLE employers
(
    employer_id int,
    employer_name varchar NOT NULL,
    description varchar,
    site_url varchar,

    CONSTRAINT pk_employers_employer_id PRIMARY KEY (employer_id)
);
CREATE TABLE vacancy
(
    vacancy_id serial,
    employer_id int,
    vacancy_name varchar,
    published_date date,
    url varchar,
    requirement varchar,
    responsibility varchar,
    experience varchar(25),
    employment varchar,
    salary_from int DEFAULT 0,
    salary_to int DEFAULT 0,

    CONSTRAINT pk_vacancy_vacancy_id PRIMARY KEY (vacancy_id),
    CONSTRAINT fk_employers_employer_id FOREIGN KEY (employer_id) REFERENCES employers(employer_id)
);
