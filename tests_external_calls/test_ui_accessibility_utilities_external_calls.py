from mashop.microtoolkit.toolkit import status_codes, APIError
import unittest

from conftest import Request, Response
from mashop.api.ui_accessibility_utilities import http_get


class TestUiAccessibilityUtilitiesSuccess(unittest.TestCase):
    def setUp(self):
        self.req = Request(params={"color": ["221", "182", "137"]})
        self.resp = Response()
        self.params = {}

    def test_external_get_ui_accessibility_utilities_mocked(self):
        # ---------- call method ----------
        http_get(self.req, self.resp, self.params)

        # ---------- evaluate response ----------
        self.assertEqual(self.resp.status, status_codes.HTTP_OK)


class TestUiAccessibilityUtilitiesFailures(unittest.TestCase):
    def setUp(self):
        self.resp = Response()
        self.params = {}

    def test_external_get_ui_accessibility_utilities_invalid_param_name_mocked(self):
        self.req = Request(params={"clor": ["221", "182", "137"]})
        # ---------- call method ----------
        with self.assertRaises(APIError) as context:
            http_get(self.req, self.resp, self.params)

        # ---------- evaluate response ----------
        self.assertEqual(context.exception.code, 'Invalid Input: color')

    def test_external_get_ui_accessibility_utilities_not_3_values_mocked(self):
        self.req = Request(params={"color": ["221", "182"]})
        # ---------- call method ----------
        with self.assertRaises(APIError) as context:
            http_get(self.req, self.resp, self.params)

        # ---------- evaluate response ----------
        self.assertEqual(context.exception.code, 'Insufficient number of Input: color')

    def test_external_get_ui_accessibility_utilities_invalid_input_mocked(self):
        self.req = Request(params={"color": ["221", "182", "aa"]})
        # ---------- call method ----------
        with self.assertRaises(APIError) as context:
            http_get(self.req, self.resp, self.params)

        # ---------- evaluate response ----------
        self.assertEqual(context.exception.code, f'Invalid Input: {self.req.params.get("color")} not a number')

if __name__ == '__main__':
    unittest.main()
