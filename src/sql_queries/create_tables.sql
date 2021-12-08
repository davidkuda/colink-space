CREATE TABLE IF NOT EXISTS users (
    user_id UUID PRIMARY KEY NOT NULL,
    name varchar(256),
    email varchar(256) UNIQUE
);

CREATE TABLE IF NOT EXISTS spaces (
    space_id UUID NOT NULL PRIMARY KEY,
    space_name varchar(256),
    creation_date date NOT NULL
);

CREATE TABLE IF NOT EXISTS space_owners (
    space_id UUID NOT NULL PRIMARY KEY,
    user_id UUID REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS space_contributors (
    space_id UUID REFERENCES spaces(space_id),
    user_id UUID REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS links (
    link_id UUID NOT NULL PRIMARY KEY,
    url varchar(512) NOT NULL UNIQUE,
    title varchar(1024),
    description varchar(2048),
    image_url varchar(1024)
);

CREATE TABLE IF NOT EXISTS posts (
    post_id UUID NOT NULL PRIMARY KEY,
    link_id UUID REFERENCES links(link_id),
    space_id UUID NOT NULL REFERENCES spaces(space_id),
    user_id UUID NOT NULL REFERENCES users(user_id),
    description varchar(512),
    date date
);
