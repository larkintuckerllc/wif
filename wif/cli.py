"""Provide an example module."""
import click
from google.cloud import storage



@click.command()
def cli():
    storage_client = storage.Client()
    click.echo('1')
    buckets = storage_client.list_buckets()
    click.echo('2')
    for bucket in buckets:
        click.echo(bucket.name)
