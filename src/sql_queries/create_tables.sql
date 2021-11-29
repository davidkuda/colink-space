CREATE TABLE IF NOT EXISTS users {
    user_id serial NOT NULL,
    name varchar(256),
    email varchar(256),
};

CREATE TABLE IF NOT EXISTS countries {
    country_id serial NOT NULL PRIMARY KEY,
    country varchar(256) NOT NULL
};

CREATE TABLE IF NOT EXISTS users_countries_map {
    country_id integer NOT NULL REFERENCES(countries.country_id),
    user_id integer NOT NULL REFERENCES(users.user_id)
};

CREATE TABLE IF NOT EXISTS professions {
    profession_id serial PRIMARY KEY,
    profession varchar(256)
};

CREATE TABLE IF NOT EXISTS users_professions_map {
    user_id integer NOT NULL REFERENCES(users.user_id),
    profession_id integer NOT NULL REFERENCES(professions.profession_id)
};

CREATE TABLE IF NOT EXISTS interests {
    interest_id serial NOT NULL PRIMARY KEY,
    interest varchar(256) NOT NULL
};

CREATE TABLE IF NOT EXISTS users_interests_map {
    user_id integer NOT NULL REFERENCES(users.user_id),
    interest_id integer NOT NULL REFERENCES(interests.interest_id)
};


CREATE TABLE IF NOT EXISTS spaces {
    space_id serial NOT NULL PRIMARY KEY,
    space_name varchar(256),
    creation_date date NOT NULL
};

CREATE TABLE IF NOT EXISTS space_owners {
    space_id serial NOT NULL PRIMARY KEY,
    user_id integer REFERENCES(users.user_id)
};

CREATE TABLE IF NOT EXISTS space_contributors {
    space_id integer REFERENCES(spaces.space_id),
    user_id integer REFERENCES(users.user_id)
};

CREATE TABLE IF NOT EXISTS links {
    url_id serial NOT NULL PRIMARY KEY,
    url varchar(512) NOT NULL,
    meta_title varchar(256),
    meta_description varchar(256),
    thumbnail_url varchar(256)
};

CREATE TABLE IF NOT EXISTS posts {
    post_id serial NOT NULL PRIMARY KEY,
    url_id integer REFERENCES(links.url),
    space_id integer NOT NULL REFERENCES(spaces.space_id),
    description varchar(512),
    date date
};
