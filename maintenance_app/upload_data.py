from typing import Any

import asyncpg


async def upload_data_to_lakehouse(settings: dict[str, Any]) -> None:
	async with asyncpg.create_pool(
		**settings['DB_CONNECTION'],
		min_size = 1,
		max_size = 4,
		max_inactive_connection_lifetime = 30.0,
	) as postgress_pool:
		# TODO: Add uploading metrics to the DB
		pass
