#! /bin/bash
set -eu

PACKAGE_PATH=$(dirname $0)
cd $PACKAGE_PATH
echo "pwd: `pwd`"
echo "\$0: $0"
echo "basename: `basename $0`"
echo "dirname: `dirname $0`"
echo "dirname/readlink: $(dirname $(readlink -f $0))"
echo "Package path: ${PACKAGE_PATH}"

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