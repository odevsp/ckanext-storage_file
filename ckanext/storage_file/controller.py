from logging import getLogger
from ckan.lib.base import request, BaseController, abort, json

import json
import pylons.config as config

log = getLogger(__name__)

class Resource_fileController(BaseController):

	def create_file(self,file_route,received_data):

		file = open(file_route, "w")
		file.truncate()
		file.write(received_data)    
		file.close()

	def validate_json(self,received_data):

		try:
			json_object = json.loads(received_data)
		except ValueError, e:
			return False
		return True

	def change_persisted_file(self):

		if not request.body:
			abort(405, 'No data POST')

		content_type = request.headers.get('Content-Type', '')

		if not content_type.startswith('application/json'):
			abort(415, 'Content-Type should be "application/json"')

		received_data=request.body;

		file_route = config.get('ckan.storage_file.route_file') 

		json_validate = self.validate_json(received_data)

		if json_validate:
			self.create_file(file_route,received_data)
		else:
			abort(400, 'Wrong Syntax')
		