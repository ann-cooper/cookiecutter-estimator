from setuptools import find_packages, setup

setup(
    name="{{cookiecutter.project_slug}}",
    version="0.1.0",
    description="{{cookiecutter.description}}",
    url="{{cookiecutter.url}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
    packages=find_packages(),
    python_requires=">=3.7",
)
