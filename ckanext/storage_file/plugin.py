from logging import getLogger

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from pylons import config

log = getLogger(__name__)

class Storage_FilePlugin(plugins.SingletonPlugin):
	plugins.implements(plugins.IConfigurer)
	plugins.implements(plugins.IRoutes, inherit=True)

	# IConfigurer

	def update_config(self, config_):
		toolkit.add_template_directory(config_, 'templates')
		toolkit.add_public_directory(config_, 'public')
		toolkit.add_resource('fanstatic', 'storage_file')

	def before_map(self, map):
		map.connect('/Persisted_json',
					controller='ckanext.storage_file.controller:Resource_fileController',
					action='change_persisted_file')
		return map