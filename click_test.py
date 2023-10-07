import click


@click.command()
@click.option(
    "--name", default="World", prompt="Your name", help="The person to greet."
)
def greet(name):
    click.echo(f"Hello, {name}!")


if __name__ == "__main__":
    greet()
