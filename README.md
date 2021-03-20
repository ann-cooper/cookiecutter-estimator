## Managing dependencies
- Dependencies are managed with pip-tools.
- To update or change dependencies, activate the venv, install pip-tools with `pip install pip-tools`
- Adjust packages listed in requirements/main.in as needed.
- To re-output the main.txt: `pip-compile requirements/main.in --output-file=- > requirements/main.txt`
- To upgrade the packages: `pip-compile requirements/main.txt`

## How to run the tests
- To run tests on this cookiecutter repo, use the Docker container: `docker build -t estimator -f Dockerfile .; docker run -it --name estimator-container -t estimator:latest`
- To stop and remove the container: `docker stop estimator-container; docker rm estimator-container`

## Creating a new customized estimator
- Run the build script from this project with `bash build.sh`
- This will interactively create the number of work types you want to define and then run the cookiecutter to create your estimator.

## Setting up the new estimator in its own directory
- Run the script to move your new estimator to another directory and clean up the project structure with: `bash <your_new_project_directory>setup_project.sh`
- By default, your new project directory will be called quick_estimator.
- When you run build.sh, it will create your new project as a subdirectory inside this cookiecutter project. When you're ready to move it and start using it, call the setup_project.sh script inside your newly created subdirectory *from this cookiecutter project*.