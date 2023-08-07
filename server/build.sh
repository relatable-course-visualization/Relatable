#!/bin/bash

# Build the project
python3.9 -m pip install django
python3.9 -m pip install pymysql
python3.9 -m pip install dj_database_url 
python3.9 -m pip install environ
echo "Building the project..."
python3.9 -m pip install -r requirements.txt
echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput
echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear