# Work Points Estimator Cookiecutter
This is a customizable points estimator for your common types of projects. 

## How to run it locally
- Cd into this project directory and run `bash build.sh`, which will ask you how many project types you want to define and then run cookiecutter to generate the customized project.
- Then, also from this project directory, call `bash {{ cookiecutter.project_slug }}/setup_project.sh your/target/directory`.
- For example: `bash quick_estimator/setup_project.sh --$HOME/git/mynewproject`
- When you run setup_project.sh, a venv will be created for you in $HOME/.venvs/{{ cookiecutter.project_slug }}.
- Activate the venv: `$HOME/.venvs/{{ cookiecutter.project_slug }}/bin/activate` 
- Run the estimator: `python {{ cookiecutter.project_slug }}/estimator.py --help`

## Managing dependencies
- Dependencies are managed with pip-tools.
- To update or change dependencies, activate the venv, install pip-tools with `pip install pip-tools`
- Adjust packages listed in requirements/main.in as needed.
- To re-output the main.txt: `pip-compile requirements/main.in --output-file=- > requirements/main.txt`
- To upgrade the packages: `pip-compile requirements/main.txt`

## How to run the tests
- To run tests *in this repo*, use the Docker container: `docker build -t estimator -f Dockerfile .; docker run -it --name estimator-container -t estimator:latest`
- To stop and remove the container: `docker stop estimator-container; docker rm estimator-container`
- To run tests *in the target directory* (after moving everything with setup_project.sh), cd into the target directory, activate the venv, and run: `python3 -m pytest`.
