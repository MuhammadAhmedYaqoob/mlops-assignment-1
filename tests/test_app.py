import unittest
import json
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_predict(self):
        response = self.client.post("/predict", json={"features": [2.5, 3.1, 1.3]})
        data = json.loads(response.data)
        self.assertIn("prediction", data)

if __name__ == "__main__":
    unittest.main()
