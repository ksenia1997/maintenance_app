import click
import maintenance_app.metrics


@click.command()
@click.option('--project-path', '-p', type = str)
@click.option('--gitlab-url', '-u', type = str)
@click.option('--private-token', '-t', type = str)
@click.option('--project-name', '-n', default = None)
def main(project_path: str, gitlab_url: str, private_token: str, project_name: str):
	print('Project path: ', project_path)
	average_cyclomatic_complexity = maintenance_app.metrics.get_average_cyclomatic_complexity(project_path)
	print('average_cyclomatic_complexity: ', average_cyclomatic_complexity)
	gitlab_metrics = maintenance_app.metrics.get_gitlab_metrics(gitlab_url, private_token, project_name)
	print(gitlab_metrics)


if __name__ == '__main__':
	main()
