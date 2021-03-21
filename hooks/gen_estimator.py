import yaml
import json
import logging

from collections import OrderedDict

logger = logging.getLogger(__name__)


def get_work_types() -> int:
    work_types = input("How many project types do you want to define today? Please type a number: ") or 1

    return int(work_types)

def create_config(num: int = get_work_types()) -> dict:
    # TODO more flexible number of work factors
    work_type_pattern = {'work_factors': {}}
    # Create estimate_config.yml
    for t in range(num):
        i = t
        t = f'{{{{cookiecutter.project_type{i}}}}}'
        work_type_pattern['work_factors'][t] = {}
        work_type_pattern['work_factors'][t]['simple'] = [
            f'{{{{cookiecutter.project_type{i}_a_simple_factor_1}}}}', 
            f'{{{{cookiecutter.project_type{i}_a_simple_factor_2}}}}',
            f'{{{{cookiecutter.project_type{i}_a_simple_factor_3}}}}',
            f'{{{{cookiecutter.project_type{i}_a_simple_factor_4}}}}'
            ]
        work_type_pattern['work_factors'][t]['complex'] = [
            f'{{{{cookiecutter.project_type{i}_complex_factor_1}}}}', 
            f'{{{{cookiecutter.project_type{i}_complex_factor_2}}}}',
            f'{{{{cookiecutter.project_type{i}_complex_factor_3}}}}',
            f'{{{{cookiecutter.project_type{i}_complex_factor_4}}}}'
            ]
    
    with open('{{cookiecutter.project_slug}}/estimate_config.yml', 'w') as f:
        yaml.dump(work_type_pattern, f)
    return work_type_pattern

def update_cookiecutter_variables(d: dict = create_config()):
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

if __name__ == "__main__":
    update_cookiecutter_variables()