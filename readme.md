# Steps to set up and run the project

# Make sure that you have python 3.9 or greater is installed
# create virtual environment
    python3 -m venv .venv (linux/mac)

# activate the virtual environment
    source .venv/bin/activate (mac)

# install the requirements from requirements.txt
    pip install -r requirements.txt

# run the commands to set up db
    python manage.py makemigrations
    python manage.py migrate

# run the server
    python manage.py runserver 0.0.0.0:8000

# APIs to set up in postman
    look at the apis.json file


