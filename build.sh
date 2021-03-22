#!/bin/bash
#
# Script to create a new customized project from this cookiecutter
#
PACKAGE_PATH=$1
echo ${PACKAGE_PATH}
python ${PACKAGE_PATH}/cookiecutter-estimator/hooks/gen_estimator.py

cookiecutter ${PACKAGE_PATH}/cookiecutter-estimator/