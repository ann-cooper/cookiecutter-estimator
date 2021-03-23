from hooks import gen_estimator

import logging


logger = logging.getLogger(__name__)


# Mock.patch get_work_types

# pytest.mark this test to only run with build-test.sh
def test_create_config():
    assert False