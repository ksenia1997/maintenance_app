import dataclasses
import datetime


@dataclasses.dataclass
class GitlabProjectAttributes:
	id: int
	name: str
	created_at: datetime.datetime
	last_activity_at: datetime.datetime
	opened_merge_requests_number: int
	closed_merge_requests_number: int
	merged_merge_requests_number: int
