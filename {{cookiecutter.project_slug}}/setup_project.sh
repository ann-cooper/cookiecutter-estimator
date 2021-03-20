#!/bin/bash
#
# Script to move the new project into the target directory and rearrange the project structure
# Call this from cookiecutter directory

# Pass in path to target 
TARGET_DIR=$1
echo ${TARGET_DIR}
# move quick_estimator to target
mv ./{{ cookiecutter.project_slug }} ${TARGET_DIR}
# move tests out 
mv ${TARGET_DIR}/{{ cookiecutter.project_slug }}/tests ${TARGET_DIR}
# move requirements out
mv ${TARGET_DIR}/{{ cookiecutter.project_slug }}/requirements ${TARGET_DIR}
# move setup.py out
mv ${TARGET_DIR}/{{ cookiecutter.project_slug }}/setup.py ${TARGET_DIR}
# move create_venv.sh out
mv ${TARGET_DIR}/{{ cookiecutter.project_slug }}/create_venv.sh ${TARGET_DIR}
# move .gitignore out
mv ${TARGET_DIR}/{{ cookiecutter.project_slug }}/.gitignore ${TARGET_DIR}
# move pytest.ini out
mv ${TARGET_DIR}/{{ cookiecutter.project_slug }}/pytest.ini ${TARGET_DIR}


echo "Create the venv with: bash ${TARGET_DIR}/create_venv.sh"
echo "Activate the venv with: source $HOME/.venvs/{{cookiecutter.project_slug}}/bin/activate"
