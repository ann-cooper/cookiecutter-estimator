import yaml
import json
import logging

from collections import OrderedDict

logger = logging.getLogger(__name__)


def get_work_types() -> tuple:
    """Asks for input to determine number of project types and number of work factors to define."""

    inputs = input("How many project types and work factors do you want to define today? Please type two numbers, the first for project and the second for work factors, like this: 2, 4 ")
    work_types, work_factors = inputs.split(',')
    return int(work_types), int(work_factors)


def create_config(type_num: int, factors_num: int) -> dict:
    """Generates a config.yaml that the estimator will use to show options and a dictionary with the 
    needed cookiecutter template variables to customize.

    Parameters
    ----------
    type_num: int
        The number of project types to define with cookiecutter.
    factors_num: int
        The number of work factors to define for each project type.
    
    Returns
    -------
    work_type_pattern: dict
        The dictionary that was used to create the yaml.
    """

    work_type_pattern = {'work_factors': {}}
    # Create estimate_config.yml
    for t in range(type_num):
        i = t
        t = f'{{{{cookiecutter.project_type{i}}}}}'
        work_type_pattern['work_factors'][t] = {}
        work_type_pattern['work_factors'][t]['simple'] = [f'{{{{cookiecutter.project_type{i}_a_simple_factor_{ix}}}}}' for ix in range(factors_num)]
        work_type_pattern['work_factors'][t]['complex'] = [f'{{{{cookiecutter.project_type{i}_complex_factor_{ix}}}}}' for ix in range(factors_num)]

    with open('{{cookiecutter.project_slug}}/estimate_config.yml', 'w') as f:
        yaml.dump(work_type_pattern, f)
    return work_type_pattern

def update_cookiecutter_variables(d: dict) -> json:
    """Uses the work_type_pattern defined by the user to write the cookiecutter json file."""
    # Add needed keys to cookiecutter.json based on input
    with open('cookiecutter.json', 'r') as f:
        data = json.load(f)

    for key, value in d['work_factors'].items():
        key = key.strip('{{}}').split('cookiecutter.')[1]
        data[key] = 'project_type'
        for subkey, v in value.items():
            for factor in v:
                factor = factor.strip("{{}}").split('cookiecutter.')[1]
                data[factor] = 'A work item associated with this type'
    ordered_data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
    with open('cookiecutter.json', 'w') as f:
        logger.info("Cookiecutter created!")
        json.dump(ordered_data, f)


if __name__ == "__main__":  # pragma: no cover
    work_types, work_factors = get_work_types()
    update_cookiecutter_variables(create_config(work_types, work_factors))