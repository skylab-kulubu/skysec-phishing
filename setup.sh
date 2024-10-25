#!/bin/bash

docker compose up -d db
sleep 60
docker compose up -d app
sleep 60
docker compose up -d nginx

docker compose exec -it app ./manage.py makemigrations
docker compose exec -it app ./manage.py migrate
docker compose exec -it app ./manage.py makemigrations