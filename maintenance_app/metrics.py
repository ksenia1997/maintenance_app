from typing import Optional
import decimal
import re
import subprocess

import gitlab
import gitlab.v4.objects.projects

import maintenance_app.data_types


def get_average_cyclomatic_complexity(project_path: str) -> decimal.Decimal:
	'''
	Calculate average cyclomatic complexity for the project.
	:param project_path: path to the project. Example: /home/researcher/project/
	:return: average cyclomatic complexity
	'''
	# TODO: Improve: Create detailed structure for each Function, Class and Method in the project.
	# TODO: Improve: add radon params to the function arguments.
	output_bytes = subprocess.check_output(f'radon cc {project_path} -a ', shell = True)
	output_str = output_bytes.decode('utf-8')
	average_complexity = decimal.Decimal(re.findall(r'\d+.\d+', output_str.split('Average complexity:')[-1])[0])
	return average_complexity


def get_gitlab_project_attributes(
	project: gitlab.v4.objects.projects.Project,
) -> maintenance_app.data_types.GitlabProjectAttributes:
	return maintenance_app.data_types.GitlabProjectAttributes(
		id = project.id,
		name = project.name,
		created_at = project.created_at,
		last_activity_at = project.last_activity_at,
		opened_merge_requests_number = len(project.mergerequests.list(state = 'opened', get_all = True)),
		closed_merge_requests_number = len(project.mergerequests.list(state = 'closed', get_all = True)),
		merged_merge_requests_number = len(project.mergerequests.list(state = 'merged', get_all = True)),
	)


def get_gitlab_metrics(
	gitlab_url: str,
	private_token: str,
	project_name: Optional[str] = None,
) -> Optional[list[maintenance_app.data_types.GitlabProjectAttributes]]:
	gl = gitlab.Gitlab(gitlab_url, private_token = private_token)
	projects = []
	for project in gl.projects.list(iterator = True):
		if project_name is None:
			projects.append(get_gitlab_project_attributes(project))
		elif project.name == project_name:
			return [get_gitlab_project_attributes(project)]
	return projects
