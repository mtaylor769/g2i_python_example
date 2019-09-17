#!/bin/bash
python3 -m venv env
. env/bin/activate
pip install --upgrade Flask
pip install --upgrade -r /src/requirements.txt -t lib

export FLASK_ENV=development
export FLASK_APP=/src/main.py
flask run --host=0.0.0.0

eval "$@"
