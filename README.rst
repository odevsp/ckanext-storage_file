-.. You should enable this project on travis-ci.org and coveralls.io to make
-   these badges work. The necessary Travis and Coverage config files have been
-   generated for you.
-
-.. image:: https://travis-ci.org//ckanext-storage_file.svg?branch=master
-    :target: https://travis-ci.org//ckanext-storage_file
-
-.. image:: https://coveralls.io/repos//ckanext-storage_file/badge.png?branch=master
-  :target: https://coveralls.io/r//ckanext-storage_file?branch=master
-
-.. image:: https://pypip.in/download/ckanext-storage_file/badge.svg
-    :target: https://pypi.python.org/pypi//ckanext-storage_file/
-    :alt: Downloads
-
-.. image:: https://pypip.in/version/ckanext-storage_file/badge.svg
-    :target: https://pypi.python.org/pypi/ckanext-storage_file/
-    :alt: Latest Version
-
-.. image:: https://pypip.in/py_versions/ckanext-storage_file/badge.svg
-    :target: https://pypi.python.org/pypi/ckanext-storage_file/
-    :alt: Supported Python versions
-
-.. image:: https://pypip.in/status/ckanext-storage_file/badge.svg
-    :target: https://pypi.python.org/pypi/ckanext-storage_file/
-    :alt: Development Status
-
-.. image:: https://pypip.in/license/ckanext-storage_file/badge.svg
-    :target: https://pypi.python.org/pypi/ckanext-storage_file/
-    :alt: License
-

=============
ckanext-storage_file - Replace persisted file through HTTP POST
=============

HTTP POST


www.yourDomain.com/Persisted_json

Content Body:

=======
	www.yourDomain.com/Persisted_json

Content Body:


	{"file/22220310180300/dataset_example.json": {"_label": "file/22220310180300/dataset_example.json", "uploaded-by": "ckan_admin" .......

------------
Requirements
------------



=======
1. You need to be Ckan administrator to access this method.


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


http://www.fsf.org/licensing/licenses/agpl-3.0.html
=======
http://www.fsf.org/licensing/licenses/agpl-3.0.html

