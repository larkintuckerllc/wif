"""Provide an example module."""
import click
from google.cloud import storage



@click.command()
def cli():
    storage_client = storage.Client()
    buckets = storage_client.list_buckets()
    for bucket in buckets:
        click.echo(bucket.name)
