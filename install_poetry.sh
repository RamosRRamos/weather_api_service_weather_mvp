#!/bin/sh

# Instala o Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Instala as dependências do Poetry
poetry install

# Executa o gunicorn com o Poetry
poetry run gunicorn weather_api_service.wsgi --log-file -
