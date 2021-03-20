#!/bin/bash
#
# Script called by Dockerfile to test the cookiecutter project using a no-input project generated in the container.
#

echo -e 1 | python hooks/gen_estimator.py

cookiecutter . --no-input

python3 -m pytest quick_estimator/tests