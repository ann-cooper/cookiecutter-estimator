"""
Load data for development or testing. Add options for addition work types.

Examples:
    python {{cookiecutter.project_slug}}/estimate.py --{{cookiecutter.project_type0}}

Usage:
    estimate.py --{{cookiecutter.project_type0}} |  --help

Options:
    --{{cookiecutter.project_type0}}
    --help

"""

import logging
from collections import Counter

import enquiries
import yaml
from docopt import docopt
from {{cookiecutter.project_slug}}.src.rules import PointsRules

logger = logging.getLogger(__name__)


def profile_issue(options: list, work_factors: dict) -> tuple:
    """Returns number of simple work factors chosen, number of complex work factors chosen, and a counter including the chosen work factors."""
    opt = options[0]
    factors = [
        (key, factor) for key, values in work_factors[opt].items() for factor in values
    ]
    choices = enquiries.choose(
        "Choose the work factors your issue involves:", factors, multi=True
    )
    counts = Counter([x for tup in choices for x in tup])

    return (counts["simple"], counts["complex"], counts)


def estimate_points(profile: tuple) -> tuple:
    """Returns a point estimate and set of selected work factors."""
    simple, complex, counts = profile

    work_factors = {k for k, v in counts.items() if k not in ['simple', 'complex']}

    est = PointsRules(simple, complex).estimate()
    if est.est:
        logger.info(f"Project estimate: {est.est}")
    else:
        logger.info(f"Input valid: {est.valid} ... too many points evaluation: {est.too_many_points}")
    return est, work_factors


def get_resource(arguments: dict) -> list:
    """Returns a list of selected options."""
    options = [k.strip("--") for k, v in arguments.items() if v]

    return options


if __name__ == "__main__":  # pragma: no cover
    arguments = docopt(__doc__)
    with open("{{cookiecutter.project_slug}}/estimate_config.yml") as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
    options = get_resource(arguments)
    estimate_points(profile_issue(options, conf["work_factors"]))
