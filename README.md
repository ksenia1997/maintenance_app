# Maintenance metrics

This application calculates cyclomatic complexity and metrics from Gitlab.


```commandline
python -m maintenance_app metrics -p [PATH_TO_PROJECT] -u [GITLAB_URL] -t [GITLAB_TOKEN_NAME] -n edge
```

```text
OUTPUT: 
Project path:  [PATH_TO_PROJECT]
average_cyclomatic_complexity:  2.753717472118959
[GitlabProjectAttributes(id=10, name='PROJECT', created_at='2015-11-13T14:41:41.470Z', last_activity_at='2023-05-10T12:45:33.770Z', opened_merge_requests_number=45, closed_merge_requests_number=622, merged_merge_requests_number=3438)]
```