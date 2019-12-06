
# testTask112019

python  command line utility ... test task for this year

## libraries

* [Click](https://click.palletsprojects.com/en/7.x/)
* [sqlalchemy](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91)
* [alembic](https://alembic.sqlalchemy.org/)
* [jsonlines](https://jsonlines.readthedocs.io/en/latest/)

## Task description

* [Task 1](https://docs.google.com/document/d/1FwndaKyc3Ua8z0tJTnv34nf3Ass4VigaemGeGNDXkGA/edit?usp=sharing) unfinished

## How to run

* install local libs `pipenv install`
* activate virtualenv|shell `pipenv shell`
* you need to run `docker-compose -f docker/postgresql.yaml`
* run db migrations `alembic upgrade head`
* then install in development mode `pip install -e .`
* and run `testtask112019 importdata --help` and `testtask112019 importdata --path <path to the folder with dada>`


### credits

This package was created with Cookiecutter_ and the `elgertam/cookiecutter-pipenv`_ project template, based on `audreyr/cookiecutter-pypackage`_.
