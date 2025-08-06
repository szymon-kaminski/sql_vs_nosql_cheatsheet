import click

@click.group()
def cli():
    """Interaktywna ściąga SQL vs NoSQL 📚"""
    click.echo("Witaj w interaktywnej ściądze SQL vs NoSQL!")

if __name__ == "__main__":
    cli()