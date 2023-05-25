# Maintenance metrics

This application calculates cyclomatic complexity and metrics from Gitlab.


```commandline
python  maintenance_app/__init__.py -p /home/ksenia/PROJECT/ -u [GITLAB_URL] -t [GITLAB_TOKEN_NAME] -n edge
```

```text
OUTPUT: 
Project path:  /home/ksenia/PROJECT/
average_cyclomatic_complexity:  2.753717472118959
[GitlabProjectAttributes(id=10, name='PROJECT', created_at='2015-11-13T14:41:41.470Z', last_activity_at='2023-05-10T12:45:33.770Z', opened_merge_requests_number=45, closed_merge_requests_number=622, merged_merge_requests_number=3438)]
```