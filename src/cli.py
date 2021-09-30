import click

from src.check_ip import CheckIp


@click.command()
def check_ip():
    """Simple program that tells you your current public IP address."""
    try:
        check_ip = CheckIp()
        click.echo(check_ip.check())
    except:
        click.echo("Error: no connectivity", err=True, color=True)


if __name__ == "__main__":
    check_ip()
