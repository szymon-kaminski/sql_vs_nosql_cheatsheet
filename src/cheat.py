import click

@click.group()
def cli():
    """Interaktywna ściąga: SQL vs NoSQL"""
    pass

@cli.command()
def sql():
    """Wyświetla informacje o bazach SQL"""
    click.echo("- SQL - relacyjne bazy danych")
    click.echo("- Dane przechowywane w tabelach (wiersze i kolumny)")
    click.echo("- Silne schematy i relacje między tabelami")
    click.echo("- Przykładowy język: SQL (Structured Query Language)")
    click.echo("Przykład zapytania:")
    click.echo("SELECT * FROM users WHERE age > 30;")

if __name__ == "__main__":
    cli()
