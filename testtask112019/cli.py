# -*- coding: utf-8 -*-

"""Console script for testtask112019."""
import sys
import click
from testtask112019.fhir import import_data
from testtask112019.task2 import sort_matrix_clockwise

# @click.command()
# def main(args=None):
#     """Console script for testtask112019."""
#     click.echo("Replace this message by putting your code into "
#                "testtask112019.cli.main")
#     click.echo("See click documentation at http://click.pocoo.org/")
#     return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover


@click.group()
def main():
    pass


@click.command()
def initdb():
    click.echo('Initialized the database')


@click.command()
def dropdb():
    click.echo('Dropped the database')


@click.command()
@click.option('--path', default='/home/xxx/TestTasks/flat-fhir-files/r3', help='path to the folder with data')
def importdata(path):
    click.echo(f'import data from ndjson {path}')
    results = import_data(path)
    for result in results:
        click.echo(result)


@click.command()
@click.option('--size-x', default=3, help='matrix size x')
@click.option('--size-y', default=3, help='matrix size y')
def snail(size_x, size_y):
    click.echo(sort_matrix_clockwise(size_x, size_y))


main.add_command(initdb)
main.add_command(dropdb)
main.add_command(importdata)
main.add_command(snail)
