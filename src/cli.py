import click

from src.check_ip import CheckIp


@click.command()
def check_ip():
    """Simple program that tells you your current public IP address."""
    check_ip = CheckIp()
    click.echo(check_ip.check())


if __name__ == "__main__":
    check_ip()
