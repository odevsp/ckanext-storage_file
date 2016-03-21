=============
ckanext-storage_file - Replace persisted file through HTTP POST
=============

HTTP POST

<<<<<<< HEAD
www.yourDomain.com/Persisted_json

Content Body:

=======
	www.yourDomain.com/Persisted_json

Content Body:

>>>>>>> 21852b57c0cda8844981b24e1b6264a2c73e56af
	{"file/22220310180300/dataset_example.json": {"_label": "file/22220310180300/dataset_example.json", "uploaded-by": "ckan_admin" .......

------------
Requirements
------------

<<<<<<< HEAD

=======
1. You need to be Ckan administrator to access this method.
>>>>>>> 21852b57c0cda8844981b24e1b6264a2c73e56af

------------
Installation
------------


To install ckanext-storage_file:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-storage_file Python package into your virtual environment::

     pip install ckanext-storage_file

3. Add ``storage_file`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Set into config file ('development.ini' or 'production.ini'):
   
    ckan.storage_file.route_file = route_of_persisted_file

---------------
Copying and License
---------------

This material is copyright (c) 2006-2016 Open Knowledge Foundation.

It is open and licensed under the GNU Affero General Public License (AGPL) v3.0 whose full text may be found at:

<<<<<<< HEAD
http://www.fsf.org/licensing/licenses/agpl-3.0.html
=======
http://www.fsf.org/licensing/licenses/agpl-3.0.html
>>>>>>> 21852b57c0cda8844981b24e1b6264a2c73e56af
