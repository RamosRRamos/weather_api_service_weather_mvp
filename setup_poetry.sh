#!/bin/bash

# Instala o Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Coloca o Poetry no PATH
export PATH="$HOME/.local/bin:$PATH"

# Instala as dependências
poetry install
