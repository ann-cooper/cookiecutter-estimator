from pathlib import Path

import pytest
import yaml


def find_path():

    paths = [
        Path("tests/test_resources/estimate_config.yml"),
        Path("{{cookiecutter.project_slug}}/tests/test_resources/estimate_config.yml"),
    ]
    for path in paths:
        if path.exists():
            return path


@pytest.fixture(scope="function")
def load_test_config(path=find_path()):
    """Load work_factors dictionary from yaml."""
    with open(path) as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
    return conf["work_factors"]


@pytest.fixture(scope="function")
def arguments():
    return {"--help": False, "--project_type": True}
