"""Provide an example module."""
import click


@click.command()
def cli():
    click.echo('Hello World!')
