#!/bin/bash

source ./venv/**/activate

cd backend && python manage.py runserver &
cd frontend && npm run dev