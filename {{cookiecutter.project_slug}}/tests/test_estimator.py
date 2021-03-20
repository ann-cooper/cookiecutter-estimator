from unittest import mock

import enquiries
import pytest
from {{cookiecutter.project_slug}}.src import estimator

try:
    from tests import params
except ModuleNotFoundError:
    from {{cookiecutter.project_slug}}.tests import params


@pytest.fixture(scope="function")
def stub_choices():
    return [("simple", "A"), ("simple", "B"), ("complex", "E")]


@pytest.mark.parametrize(
    "id, options,  expected", params.profile_params, ids=params.profile_ids
)
def test_profile_issue(load_test_config, stub_choices, id, options, expected):
    with mock.patch("enquiries.choose", autospec=True) as mock_choices:
        mock_choices.return_value = stub_choices
        simple, complex, counts = estimator.profile_issue(options, load_test_config)

        assert expected["simple"] == simple
        assert expected["complex"] == complex
        assert expected["counts"] == counts


@pytest.mark.parametrize(
    "id, profile, expected_est, expected_work_factors",
    params.estimate_points,
    ids=params.estimate_points_ids,
)
def test_estimate_points(id, profile, expected_est, expected_work_factors):

    est, work_factors = estimator.estimate_points(profile)

    assert est.est == expected_est
    assert work_factors == expected_work_factors


def test_get_resource(arguments):

    options = estimator.get_resource(arguments)
    assert options[0] == "project_type"
