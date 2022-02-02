import json
import unittest

from common import Request, Response, set_environment
from mashop.api.ui_accessibility_utilities import http_get


class TestUiAccessibilityUtilities(unittest.TestCase):
    def setUp(self):
        self.req = Request()
        self.resp = Response()
        self.params = ''
        set_environment(env='POC')

    def test_get_hello_world(self):
        # ---------- call method ----------
        http_get(self.req, self.resp, self.params)

        # ---------- evaluate response ----------
        message = self.resp.body['message']

        self.assertEqual('hello world', message)


class TestUiAccessibilityUtilitiesFailures(unittest.TestCase):
    # failure tests aren't really relevant for the items that are currently in place
    pass


if __name__ == '__main__':
    unittest.main()
