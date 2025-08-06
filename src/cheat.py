import click

@click.group()
def cli():
    """Interaktywna ściąga: SQL vs NoSQL"""
    pass

@cli.command()
def sql():
    """Wyświetla informacje o bazach SQL"""
    click.echo("SQL - relacyjne bazy danych")
    click.echo("- Dane przechowywane w tabelach (wiersze i kolumny)")
    click.echo("- Silne schematy i relacje między tabelami")
    click.echo("- Przykładowy język: SQL (Structured Query Language)")
    click.echo("Przykład zapytania:")
    click.echo("SELECT * FROM users WHERE age > 30;")


@cli.command()
def nosql():
    """Pokaż cechy i przykładowe zapytania NoSQL."""
    click.echo("NoSQL - Not Only SQL")
    click.echo("- Dane przechowywane w dokumentach, klucz-wartość, grafach, itp.")
    click.echo("- Większa elastyczność struktury danych.")
    click.echo("- Przykład (MongoDB):")
    click.echo('  db.users.find({ age: { $gt: 30 } })')


if __name__ == "__main__":
    cli()
