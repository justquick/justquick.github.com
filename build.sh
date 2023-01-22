#!/bin/bash
pipenv run jinja2 templates/index.html -D year=`date +%Y` -o index.html
