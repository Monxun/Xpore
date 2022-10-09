import click
import subprocess

"""
Xpore is a tool for deploying CycleDelic applications with Dashboard.
"""

# ////////////////////////////////////////////////////////////////
# DEFINE CLI
# ////////////////////////////////////////////////////////////////

# COMMAND GROUP
@click.group()
def cli():
    pass


# INIT COMMAND
@click.command()
def init():
    """Initialize a new CycleDelic application."""

    click.echo(f"Hello! I am XPORE :)")
    choice = click.input("Do you want to create a new CycleDelic cluster locally? [y/n] ")
    if choice == "y":
        click.echo(f"Initializing a new CycleDelic cluster...")
        subprocess.call(["cd", "ansible", "&&", "sudo", "ansible-playbook", "playbook.yml", "--tags", "init"])
    else:
        click.echo("Exiting...")
        exit()


# UP COMMAND
@click.command()
def up():
    """Spin up CycleDelic cluster."""
    click.echo(f"Spinning up your CycleDelic cluster...")
    subprocess.call(["cd", "ansible", "&&", "sudo", "ansible-playbook", "playbook.yml", "--tags", "up"])


# DOWN COMMAND
@click.command()
def down():
    """Spin down CycleDelic cluster."""
    click.echo(f"Spinning down your CycleDelic cluster...")
    subprocess.call(["cd", "ansible", "&&", "sudo", "ansible-playbook", "playbook.yml", "--tags", "down"])


# ////////////////////////////////////////////////////////////////
# MAIN FUNCTION
# ////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    cli()
