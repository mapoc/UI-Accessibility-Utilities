import os
import pytest

from mashop.utilities import setup_envs


@pytest.fixture(scope='module')
def setup_env():
    # The default is local override here...
    # os.environ['APP_ENV'] = 'DEV'
    setup_envs()


@pytest.fixture(scope='module')
def setup_common_api_params():
    setup_data = {
        'req': Request(),
        'resp': Response(),
        'params': ''
    }

    return setup_data


class BaseVars(object):
    master_apikey = 'some-apikey'


class Request(object):
    def __init__(self, body=None, headers=None, context=None, path='', apikey=BaseVars.master_apikey, params=None):
        self.body = body
        if headers is None:
            headers = {'Content-Type': 'application/json', 'APIKEY': apikey}
        self.headers = headers
        self.context = context
        self.path = path
        self.apikey = apikey
        if params is None:
            params = {}
        self.params = params


class Response(object):
    def __init__(self, body='', status='200 OK'):
        self.body = body
        self.status = status
