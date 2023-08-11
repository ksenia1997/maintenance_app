from typing import Any
import importlib


def settings_load(profile: str) -> dict[str, Any]:
	'''
	Load all variables which not started with underscore and are UPPERCASED from settings.{profile} to dictionary and return it
	Example:
		`settings = tools.settings_load('develop')`
	'''
	return {
		key: value
		for key, value in vars(importlib.import_module('settings.{profile}'.format(profile = profile))).items()
		if not key.startswith('_') and key.isupper()
	}
