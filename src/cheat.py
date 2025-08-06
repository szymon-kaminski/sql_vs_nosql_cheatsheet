import click


def run_quiz():
    print("\n=== SQL vs NoSQL Quiz ===\n")
    print("Pytanie 1: Która baza danych najlepiej nadaje się do przechowywania danych o stałej strukturze?")
    print("a) SQL")
    print("b) NoSQL")
    answer1 = input("Twój wybór (a/b): ").strip().lower()
    if answer1 == "a":
        print("Dobrze! SQL jest lepszy dla danych o stałej strukturze.\n")
    else:
        print("Nie do końca. SQL jest lepszy dla danych o stałej strukturze.\n")


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


@cli.command()
def compare():
    """Compare SQL and NoSQL databases."""
    table = f"""
| Feature           | SQL                                | NoSQL                                 |
|-------------------|------------------------------------|---------------------------------------|
| Model             | Relational (tables)                | Non-relational (JSON, key-value)      |
| Schema            | Fixed                              | Dynamic / flexible                    |
| Scalability       | Vertical (scale-up)                | Horizontal (scale-out)                |
| Query Language    | SQL                                | Varies (MongoQL, etc.)                |
| Use Cases         | Structured data, ACID compliance   | Big Data, real-time apps, flexibility |
"""
    click.echo(table)


@cli.command()
def quiz():
    """Krótki quiz SQL vs NoSQL"""
    run_quiz()


if __name__ == "__main__":
    cli()
