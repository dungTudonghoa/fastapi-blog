"""Regression tests for the actual FastAPI blog application."""
import unittest
from fastapi.testclient import TestClient
from fastapi_blog.main import app

class BlogTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_home_html(self):
        r = self.client.get("/")
        self.assertEqual(r.status_code, 200)
        self.assertIn("text/html", r.headers["content-type"])

    def test_posts_list(self):
        r = self.client.get("/api/posts")
        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(r.json(), list)
        self.assertGreaterEqual(len(r.json()), 2)

    def test_get_post(self):
        r = self.client.get("/api/posts/1")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["id"], 1)

    def test_missing_post(self):
        r = self.client.get("/api/posts/999999")
        self.assertEqual(r.status_code, 404)

    def test_create_post(self):
        r = self.client.post("/api/posts", json={"author": "Tester", "title": "Merge test", "content": "Example"})
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json()["title"], "Merge test")

if __name__ == "__main__":
    unittest.main()
