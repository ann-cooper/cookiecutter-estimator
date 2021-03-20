import pytest
from {{cookiecutter.project_slug}}.src.rules import PointsRules

try:
    from tests import params
except ModuleNotFoundError:
    from {{cookiecutter.project_slug}}.tests import params


@pytest.mark.parametrize('id, simple, complex, expected_est, expected_caution', params.rules_params, ids=params.rules_ids)
def test_get_rules_valid(id, simple, complex, expected_est, expected_caution):

    guide = PointsRules(simple, complex)
    guide.estimate()

    assert guide.est == expected_est
    assert guide.too_many_points == expected_caution


@pytest.mark.parametrize('id, simple, complex, expected', params.rules_invalid, ids=params.invalid_ids)
def test_get_rules_invalid(id, simple, complex, expected):

    with pytest.raises(Exception):
        guide = PointsRules(simple, complex)
        guide.estimate()
        print(f"testing valid: {guide.valid}")
        assert guide.valid == expected
