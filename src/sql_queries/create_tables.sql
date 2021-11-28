CREATE TABLE IF NOT EXISTS users {
    userId serial NOT NULL,
    name varchar(256),
    email varchar(256),
    country varchar(256),
    profession varchar(256),
    interests varchar(256)
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
    url varchar(512) NOT NULL PRIMARY KEY,
    meta_title varchar(256),
    meta_description varchar(256),
    thumbnail_url varchar(256)
};

CREATE TABLE IF NOT EXISTS posts {
    post_id serial NOT NULL PRIMARY KEY,
    url varchar(512) REFERENCES(links.url),
    space_id integer NOT NULL REFERENCES(spaces.space_id),
    description varchar(512),
    date date
};
