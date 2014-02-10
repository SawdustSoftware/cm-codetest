# CustomMade Engineering Test
## TwitterApp
This engineering test is a simple test to guage a candidates level of competency in both python and django.

### INSTALLATION

* Configure environment variables

    * ```export DJANGO_SETTINGS_MODULE=twitterapp.settings.dev```

* Get Requirements
    * ```mkvirtualenv cm-codetest```
        * (optional) this step is optional, but we strongly recommend [virtualenv](http://www.virtualenv.org/en/latest/) + [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/).

    * ```pip install -r requirements.txt```
        * note: if you choose not to use a virtualenv, you most likely will need to use `sudo`
* Setup Database:
    * ```./manage.py syncdb``` 
    * ```./manage.py migrate```

* Run app
    * ```./manage.py runserver```



### TESTING

Bonus points if your code comes with unit or integration tests.
