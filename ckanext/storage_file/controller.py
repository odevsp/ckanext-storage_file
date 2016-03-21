from logging import getLogger
from ckan.lib.base import request, BaseController, abort, json, c
from ckan.plugins import toolkit

import ckan.logic as logic
import ckan.plugins as p
import json
import pylons.config as config
import ckan.model as model
import ckan.logic


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

		if not request.method == 'POST':
			abort(405, 'Method not allowed')

		if not c.userobj:
			abort(401, 'Forbidden, need user login')

		if not c.userobj.sysadmin:
			abort(401, 'Forbidden, need API-Key')

		if not request.body:
			abort(400, 'No body data received')

		content_type = request.headers.get('Content-Type', '')

		if not content_type.startswith('application/json'):
			abort(415, 'Content-Type should be "application/json"')

		received_data=request.body

		file_route = config.get('ckan.storage_file.route_file') 

		json_validate = self.validate_json(received_data)

		if json_validate:
			self.create_file(file_route,received_data)
		else:
			abort(400, 'Wrong Syntax')