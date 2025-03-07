import unittest
import pickle
import numpy as np

class TestModel(unittest.TestCase):
    def setUp(self):
        with open("model.pkl", "rb") as file:
            self.model = pickle.load(file)

    def test_prediction_output(self):
        sample_input = np.array([2.5, 3.1, 1.3]).reshape(1, -1)
        prediction = self.model.predict(sample_input)
        self.assertIn(prediction[0], [0, 1])

if __name__ == "__main__":
    unittest.main()
