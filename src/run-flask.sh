#!/bin/sh
export FLASK_APP=./api.py
flask --debug run -h 0.0.0.0
