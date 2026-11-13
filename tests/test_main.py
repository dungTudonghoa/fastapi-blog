"""Regression tests for the existing public API."""

import unittest

from fastapi.testclient import TestClient

from main import app


class RootEndpointTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_get_root_returns_hello_world(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World"})

    def test_get_root_returns_json(self) -> None:
        response = self.client.get("/")
        self.assertTrue(response.headers["content-type"].startswith("application/json"))


if __name__ == "__main__":
    unittest.main()
