import click

import maintenance_app.metrics.metrics


@click.group()
def cli() -> None:
	pass


cli.add_command(maintenance_app.metrics.metrics.metrics)

if __name__ == '__main__':
	cli()  # pylint: disable=[no-value-for-parameter]
