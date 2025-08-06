import click


def run_quiz():
    print("\n=== SQL vs NoSQL Quiz ===\n")
    questions = [
        {
            "question": "Która baza danych najlepiej nadaje się do przechowywania danych o stałej strukturze?",
            "options": {"a": "SQL", "b": "NoSQL"},
            "answer": "a"
        },
        {
            "question": "Która baza danych lepiej skaluje się horyzontalnie?",
            "options": {"a": "SQL", "b": "NoSQL"},
            "answer": "b"
        },
        {
            "question": "Która baza danych ma silne schematy i relacje między tabelami?",
            "options": {"a": "SQL", "b": "NoSQL"},
            "answer": "a"
        }
    ]
    
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nPytanie {i}: {q['question']}")
        for key, val in q["options"].items():
            print(f"{key}) {val}")
      
        while True:
            answer = input("Twój wybór (a/b): ").strip().lower()
            if answer in q["options"]:
                break
            else:
                print("Niepoprawna opcja, wybierz a lub b.")

        if answer == q["answer"]:
            print("Dobrze!")
            score += 1
        else:
            print(f"Źle. Poprawna odpowiedź: {q['answer']}) {q['options'][q['answer']]}")
    print(f"\nTwój wynik: {score}/{len(questions)}")


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
