CREATE TABLE IF NOT EXISTS users {
    user_id UUID NOT NULL,
    name varchar(256),
    email varchar(256),
};

CREATE TABLE IF NOT EXISTS countries {
    country_id UUID NOT NULL PRIMARY KEY,
    country varchar(256) NOT NULL
};

CREATE TABLE IF NOT EXISTS users_countries_map {
    country_id UUID NOT NULL REFERENCES(countries.country_id),
    user_id UUID NOT NULL REFERENCES(users.user_id)
};

CREATE TABLE IF NOT EXISTS professions {
    profession_id UUID PRIMARY KEY,
    profession varchar(256)
};

CREATE TABLE IF NOT EXISTS users_professions_map {
    user_id UUID NOT NULL REFERENCES(users.user_id),
    profession_id UUID NOT NULL REFERENCES(professions.profession_id)
};

CREATE TABLE IF NOT EXISTS interests {
    interest_id UUID NOT NULL PRIMARY KEY,
    interest varchar(256) NOT NULL
};

CREATE TABLE IF NOT EXISTS users_interests_map {
    user_id UUID NOT NULL REFERENCES(users.user_id),
    interest_id UUID NOT NULL REFERENCES(interests.interest_id)
};


CREATE TABLE IF NOT EXISTS spaces {
    space_id UUID NOT NULL PRIMARY KEY,
    space_name varchar(256),
    creation_date date NOT NULL
};

CREATE TABLE IF NOT EXISTS space_owners {
    space_id UUID NOT NULL PRIMARY KEY,
    user_id UUID REFERENCES(users.user_id)
};

CREATE TABLE IF NOT EXISTS space_contributors {
    space_id UUID REFERENCES(spaces.space_id),
    user_id UUID REFERENCES(users.user_id)
};

CREATE TABLE IF NOT EXISTS links {
    url_id UUID NOT NULL PRIMARY KEY,
    url varchar(512) NOT NULL,
    meta_title varchar(256),
    meta_description varchar(256),
    thumbnail_url varchar(256)
};

CREATE TABLE IF NOT EXISTS posts {
    post_id UUID NOT NULL PRIMARY KEY,
    url_id UUID REFERENCES(links.url),
    space_id UUID NOT NULL REFERENCES(spaces.space_id),
    user_id UUID NOT NULL REFERENCES(users.user_id),
    description varchar(512),
    date date
};
