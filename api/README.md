# PATIENT MANAGEMENT API

# Clone project

* `git@github.com:theTypan/patientManegementInterviewTask.git`
## To install

* ` $ sudo apt-get install postgresql`
* ` $ sudo apt-get install -y python3-pip`
* ` $ pip3 install virtualenv`
* ` $ virtualenv env`
* ` $ source env/bin/activate`


* cd to project folder/api
* ` $ pip install -r requirements.txt`

## Postgres

* ` $ sudo su postgres`
* ` $ psql`
* ` # CREATE DATABASE patient_task;`
* ` # CREATE USER app WITH SUPERUSER LOGIN PASSWORD app`
* ` # \q`
* ` $ exit`

## TO RUN

* `$ python manage.py makemigrations`
* `$ python manage.py migrate`
* `$ python manage.py createsuperuser`
* `$ python manage.py runserver`

## To ACCESS ADMIN

Navigate to localhost:8000/admin

## To ACCESS API

Navigate to localhost:8000
