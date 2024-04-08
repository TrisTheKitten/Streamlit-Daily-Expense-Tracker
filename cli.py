import click
from main import add_income, add_expense

@click.group()
def cli():
    pass

@cli.command()
@click.argument('amount', type=float)
@click.argument('category')
def add_income(amount, category):
    add_income(amount, category)
    click.echo(f"Income of {amount} added to category '{category}'.")

@cli.command()
@click.argument('amount', type=float)
@click.argument('category')
def add_expense(amount, category):
    add_expense(amount, category)
    click.echo(f"Expense of {amount} added to category '{category}'.")

if __name__ == '__main__':
    cli()