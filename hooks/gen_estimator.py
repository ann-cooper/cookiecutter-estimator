import yaml
import json
import logging

from collections import OrderedDict

logger = logging.getLogger(__name__)


def get_work_types() -> int:
    work_types = input("How many project types do you want to define today? Please type a number: ") or 1
    work_factors = input("How many work factors do you want to define for each project type? Please type a number: ") or 4
    return int(work_types), int(work_factors)


def create_config(type_num: int, factors_num: int) -> dict:
    # TODO more flexible number of work factors
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