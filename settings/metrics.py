import decouple # type: ignore[import]


DB_CONNECTION = {
	'host': decouple.config('DB_HOST'),
	'port': decouple.config('DB_PORT', cast = int),
	'user': decouple.config('DB_USER'),
	'password': decouple.config('DB_PASSWORD'),
	'database': decouple.config('DB_DATABASE'),
}
