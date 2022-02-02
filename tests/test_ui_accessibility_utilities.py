import json
import pytest

from common import Request, Response, set_environment
from mashop.api.ui_accessibility_utilities import http_get

@pytest.fixture(scope="module")
def micro_setup_data(setup_env, setup_common_api_params):

    return setup_common_api_params



def test_get_hello_world(micro_setup_data):
    # ---------- call method ----------
    http_get(micro_setup_data['req'], micro_setup_data['resp'], micro_setup_data['params'])

    # ---------- evaluate response ----------
    message = micro_setup_data['resp'].body['message']

    assert (message == 'hello world')
