# Data Catalog

![CoLinkSpace Data Model](https://github.com/davidkuda/media/blob/main/CoLinkSpace/data-models/colinkspace_overview.png)

This file explains the data model with the `create_tables.sql` file. Note that each field / column has an explanation as well as each table.

```sql
/* Users that sign up to use colink.space */
CREATE TABLE IF NOT EXISTS users (
    /* unique id */
    user_id UUID PRIMARY KEY NOT NULL,
    /* name of the user */
    name varchar(256),
    /* email of the user */
    email varchar(256)
);

/* Whenever a user signs up, he gets a default space. Additionally,
every user can create further spaces. A user could have for instance
a space for code links, a space for guitar links and a space for
parenting links */
CREATE TABLE IF NOT EXISTS spaces (
    /* unique id */
    space_id UUID NOT NULL PRIMARY KEY,
    /* name of the space, not required to be unique */
    space_name varchar(256),
    /* date when space was created */
    creation_date date NOT NULL
);

/* Every space needs an owner with high privileges / permissions 
such as delete or add contributors. */
CREATE TABLE IF NOT EXISTS space_owners (
    /* id of space */
    space_id UUID NOT NULL PRIMARY KEY,
    /* id of user */
    user_id UUID REFERENCES users(user_id)
);

/* A space can have multiple contributors: Contributors can read and write
which means they can add links to a space and like and comment posts. */
CREATE TABLE IF NOT EXISTS space_contributors (
    /* id of space */
    space_id UUID REFERENCES spaces(space_id),
    /* id of user */
    user_id UUID REFERENCES users(user_id)
);

/* A parsed link with meta information that will be shown as card on a space. */
CREATE TABLE IF NOT EXISTS links (
    /* unique id of a link */
    link_id UUID NOT NULL PRIMARY KEY,
    /* url such as "https://kuda.ai" */
    url varchar(512) NOT NULL UNIQUE,
    /* meta title of that page */
    title varchar(1024),
    /* meta description of that page (what gets showed in search engines) */
    description varchar(2048),
    /* An url to a preview image, if there is any */
    image_url varchar(1024)
);

/* A post in a space. */
CREATE TABLE IF NOT EXISTS posts (
    /* unique id of a post */
    post_id UUID NOT NULL PRIMARY KEY,
    /* reference to a link */
    link_id UUID REFERENCES links(link_id),
    /* reference to a space which holds that post */
    space_id UUID NOT NULL REFERENCES spaces(space_id),
    /* reference to a user who owns this post */
    user_id UUID NOT NULL REFERENCES users(user_id),
    /* description / comment to a post */
    description varchar(512),
    /* date when this post was created */
    date date
);

```