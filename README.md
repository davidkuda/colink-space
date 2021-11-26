![CoLinkSpace Logo](https://github.com/davidkuda/media/blob/main/CoLinkSpace/logo/coLinkspace-logos.jpeg?raw=true)

# CoLinkSpace

CoLink.Space has three main features:

1. Store links
2. Find and retrieve links
3. Share links with your family and friends

This repository is a POC / Proof of Concept of the underlying data model. I run two tests with this repository:

1. Test the data model with an upload of 1'000'000 records. The data will be generated randomly from sample data.
2. Get all posts listed under a space (after the upload)

## The data Model

Once a user signs up he has a basic space. A user can add posts to that space. A post contains a link, a description, tags and mentions (similar to a tweet on Twitter). A user can create multiple spaces. For example, he could use one space for himself, create a separate space to share links with his colleagues and another one to share parenting stuff with his wife.

![CoLinkSpace Data Model](https://github.com/davidkuda/media/blob/main/CoLinkSpace/data-models/colinkspace_overview.png)

## The Schema

![CoLinkSpace Schema](https://github.com/davidkuda/media/blob/main/CoLinkSpace/schemas/colinkspace-schema.drawio.png)

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
