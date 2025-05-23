import unittest
from predict_genre import predict_genre

class TestGenrePrediction(unittest.TestCase):

    def test_typical_plot(self):
        plot = "A man is sent to space to save Earth from an asteroid."
        genre = predict_genre(plot)
        self.assertIsInstance(genre, str)
        self.assertGreater(len(genre), 0)

    def test_empty_input(self):
        plot = ""
        genre = predict_genre(plot)
        self.assertIsInstance(genre, str)

    def test_gibberish_input(self):
        plot = "asdkjasldjasd asdjasd asdasd"
        genre = predict_genre(plot)
        self.assertIsInstance(genre, str)

if __name__ == '__main__':
    unittest.main()