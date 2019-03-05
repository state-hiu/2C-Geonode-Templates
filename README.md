# State-Geonode-Templates
templates for 2C-GeoNode

The Plan:

This repo will hold the modified template and static files for the State GeoNode. 

This repo is supposed to exist within the GeoNode application directory. For example, if the GeoNode application is named 'my_geonode', then this repository will be located within the 'my_geonode/my_geonode' directory.

This repo will also contain a script that will automatically load the template and static files into the right directories, and a script that will pull in modified files back into the repository before a commit.

directories to load:
-static
-templates

**extra note: When loading the templates I did 2 modifications to the settings file, which may have resulted in the proper templates and static files being loaded. They were adding this:

```
# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = os.getenv('STATIC_URL',"/static/")
```

as well as adding the 'debug toolbar' app to this code block:

```
if PROJECT_NAME not in INSTALLED_APPS:
    INSTALLED_APPS += (PROJECT_NAME,'debug_toolbar')
```

I also installed the debug toolbar:

```
pip install django-debug-toolbar
```
