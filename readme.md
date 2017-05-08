#Kwetter-DRF
This is a implementation of kwetter using Django Rest Framework. This project uses Python3. 
##First run
1. Install the dependecies using `pip install -r requirements.txt`. This will install everything you need to use the API.
   * It's recommended to use a virtualenviroment for this project for more information see [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#quick-start)
1. Create the database using `python manage.py migrate`.
1. Create a local superuser for use in the admin interface using `python manage.py createsuperuser` and fill in the required fields.
##Running the API
To start the API run `python manage.py runserver`
##Using the API
visit the API at <http://127.0.0.1:8000>