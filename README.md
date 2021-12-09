![CoLinkSpace Logo](https://github.com/davidkuda/media/blob/main/CoLinkSpace/logo/coLinkspace-logos.jpeg?raw=true)

# CoLinkSpace

CoLink.Space has three main features:

1. Store links
2. Find and retrieve links
3. Share links with your family and friends

This repository is a POC / Proof of Concept of the underlying data model. I run two tests with this repository:

1. Test the data model with an upload of 1'000'000 records. The data will be generated randomly from sample data.
2. Get all posts listed under a space (after the upload)

## The Schema

### Overview

The user signs up from a frontend. That could be:

- A command line interface
- A website
- A mobile app
- A Mac app

The frontend does not store data but relies entirely on a backend (JAM-Stack).

![CoLinkSpace Schema](https://github.com/davidkuda/media/blob/main/CoLinkSpace/schemas/colinkspace-schema.drawio.png)

### A sample post request

Whenever a user adds a new link, there is going to be a post request to the backend. The post requests is of type JSON and has the following schema:

```json
{
    "link": "https://kuda.ai (str)",
    "description": "This is my own website! (str)",
    "date": "yyyy-mm-dd (str)",
    "space_id": "uuid (str)",
    "user_id": "uuid (str)"
}
```

![CoLinkSpace Schema](https://github.com/davidkuda/media/blob/main/CoLinkSpace/schemas/colinkspace-post-request.drawio.png)

### A sample get request

Whenever a user opens his space, the frontend will fetch the data from the backend. The frontend gets data in the JSON format:

```json
{
  "data": [
    {
      "comment": "Colour-changing magnifying glass gives clear view of infrared light",
      "date": "2021-12-08",
      "description": "By trapping light into tiny crevices of gold, researchers have coaxed molecules to convert invisible infrared into visible light, creating new low-cost",
      "image_url": "https://www.cam.ac.uk/sites/www.cam.ac.uk/files/news/research/news/nanoantennas.jpg",
      "title": "Colour-changing magnifying glass gives clear view of infrared light",
      "url": "https://www.cam.ac.uk/research/news/colour-changing-magnifying-glass-gives-clear-view-of-infrared-light"
    }
  ]
}
```

![CoLinkSpace Schema](https://github.com/davidkuda/media/blob/main/CoLinkSpace/schemas/colinkspace-get-request.drawio.png)

### Origin of the data

- Users are created randomly from a list of first names and a list of last names
- Links are retrieved from Hacker News (https://news.ycombinator.com/) (web scraped)
- Meta Information on links are enriched / parsed with webpreview (https://github.com/ludbek/webpreview)


## The data Model

Once a user signs up he has a basic space. A user can add posts to that space. A post contains a link, a description, tags and mentions (similar to a tweet on Twitter). A user can create multiple spaces. For example, he could use one space for himself, create a separate space to share links with his colleagues and another one to share parenting stuff with his wife.

This means that for this project I have used a normalized, relational data model.

I am using a postgres database (single node, not distributed). This can well handle 1'000'000 records, but it would make sense to change to a distributed system if there was growth.

![CoLinkSpace Data Model](https://github.com/davidkuda/media/blob/main/CoLinkSpace/data-models/colinkspace_overview.png)

### Using the Data Model

The Data Model is useful in two ways:

1. It provides data to the frontend -> Enables the frontend to fetch content
2. It enables analytics

### Enabling Frontend to fetch app data

A frontend could make a request to the backend and ask for content. An example could be:

`curl backend.colink.space/posts?space=space_id`

The backend would query the database by joining the post table with the link table:

```sql
SELECT comment, url, title, links.description, image_url, date
FROM posts
JOIN links ON posts.link_id = links.link_id
WHERE space_id = 'space_id';
```

The backend would probably send the data with pagination. Ten sample links might look like this:

```json
{
  "data": [
    {
      "comment": "Workers quit jobs in droves to become their own bosses",
      "url": "https://www.wsj.com/articles/workers-quit-jobs-in-droves-to-become-their-own-bosses-11638199199",
      "title": "Page Not Found",
      "description": "We can’t find the page you are looking for.",
      "image_url": "https://s.wsj.net/img/meta/wsj-social-share.png",
      "date": "2021-11-30"
    },
    ...
  ]
}
```

The frontend would take this data and render it as cards in the space.

### Enable Analytics

The data model would enable to make queries to learn more about the usage of the app. You could for instance find out which link was posted the most or who is the user that is most active.

In that case, we could even form a star schema around the `posts` table. The `posts` table would be the facts table and all tables that are referenced with their respective foreign keys would be the dimension tables.

A sample query could be:

```sql
SELECT COUNT(posts.link_id) as count, url, title
FROM posts
JOIN links ON posts.link_id = links.link_id
GROUP BY links.link_id
ORDER BY count DESC
LIMIT 3;
```

And here you would find out that these links were shared most:

|count|url|title|
|-----|---|-----|
|71|https://apenwarr.ca/log/20211201|100 years of whatever this will be|
|64|https://tutanota.com/blog/posts/germany-right-to-encryption/|Germany: New government plans 'right to encryption'.|
|54|https://googleprojectzero.blogspot.com/2021/12/this-shouldnt-have-happened.html|This shouldn't have happened: A vulnerability postmortem|


## Scaling Scenarios

### What if there were 100'000'000 rows of data?

Right now I am using a single Postgres instance. Postgres would not be an appropriate choice for that amount of data. Instead, I would rather consider using a distributed database. Since the data must be written and also retrieved in real time, I would probably use a stream processing technology such as Kafka. I would not use Spark, since Spark is focussing on batch processing. The app requires real time processing, so Spark is rather inappropriate. 

### How could I make use of pipelines that run daily?

If I wanted to deploy data science models such as recommender systems I would definately create a data lake model where the app can use the data as well as the analytics. For the analytics part I would use Spark with a pipeline orchestrator such as prefect (https://www.prefect.io). 

### What if there were hundreds of requests simultaniously every second?
As in the reply above, in order to be able to process so many requests I would deploy a distributed database. Then I would definately use the cloud because scaling is built in. In Addition to a technology such as Kafka I would also need to deploy Load Balancing, Caching and CDN. It would probably make sense to prepare the backend in a container and make it available with Kubernetes. I would choose Go as the programming language since Go is very powerful in handling a lot of requests.

## Files in the repository

Make sure that you have prepared your environment. Once you did, you can run `src/etl.py`. 

You can explore the data base if you install jupyter notebooks and open the `notebooks/explore-database.ipynb`.

Make sure that you have access to a postgres database (or any other relational database that is compatible with psycopg2). If you have docker installed, just `cd` to the root of this repository and execute `docker-compose up`, this will create a postgres instance in docker. 

If you choose to use another postgres instance, make sure to update `config/dwh.cfg`.

## Getting Started

To set up your local development environment, please use a fresh virtual environment.

To create the environment run:

    conda env create --name colinkspace --file=environment-dev.yml

To activate the environment run:

    conda activate colinkspace

To update this environment with your production dependencies run:

    conda env update --file=environment.yml

You can now import functions and classes from the module with `import colinkspace`.

### Testing

We use `pytest` as test framework. To execute the tests, please run

    python setup.py test

To run the tests with coverage information, please use

    python setup.py testcov

and have a look at the `htmlcov` folder, after the tests are done.

### Notebooks

To use your module code (`src/`) in Jupyter notebooks (`notebooks/`) without running into import errors, make sure to install the source locally

    pip install -e .

This way, you'll always use the latest version of your module code in your notebooks via `import colinkspace`.

Assuming you already have Jupyter installed, you can make your virtual environment available as a separate kernel by running:

    conda install ipykernel
    python -m ipykernel install --user --name="colinkspace"

Note that we mainly use notebooks for experiments, visualizations and reports. Every piece of functionality that is meant to be reused should go into module code
and be imported into notebooks.

### Distribution Package

To build a distribution package (wheel), please use

    python setup.py dist

this will clean up the build folder and then run the `bdist_wheel` command.

### Contributions

Before contributing, please set up the pre-commit hooks to reduce errors and ensure consistency

    pip install -U pre-commit && pre-commit install

## Contact

David Kuda (david.kuda.ch at gmail.com)

## License

© David Kuda
