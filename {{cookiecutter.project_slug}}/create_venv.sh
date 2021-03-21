#! /bin/bash
set -eu

PACKAGE_PATH=$(dirname $0)
cd $PACKAGE_PATH

python3 -m venv $HOME/.venvs/{{cookiecutter.project_slug}}
source $HOME/.venvs/{{cookiecutter.project_slug}}/bin/activate

pip install --upgrade pip
pip install pip-tools
# install packages in main.in in the venv
pip-sync requirements/main.txt

# If you add or change packages in main.in, generate a new main.txt like so:
# pip-compile requirements/main.in --output-file=- > requirements/main.txt
# Upgrade packages like so:
# pip-compile requirements/main.txt