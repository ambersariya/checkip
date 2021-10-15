import click

from src.check_ip import CheckIp
import pkg_resources

package_version = pkg_resources.get_distribution("checkip").version


@click.command()
@click.version_option(package_version)
def check_ip():
    """Simple program that tells you your current public IP address."""
    try:
        check_ip = CheckIp()
        click.echo(check_ip.check())
    except:
        click.echo("Error: no connectivity", err=True, color=True)


if __name__ == "__main__":
    check_ip()
