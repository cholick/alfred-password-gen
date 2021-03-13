import unittest

from dictionary.processed import words


class TestProcess(unittest.TestCase):
    def test_lengths(self):
        keys = list(words.keys())
        keys = sorted(keys)

        self.assertEqual(4, keys[0])
        self.assertEqual(13, keys[-1])

    def test_lots(self):
        for k in words:
            self.assertGreater(len(words[k]), 2500)

    def test_no_dupes(self):
        for k in words:
            self.assertEqual(len(words[k]), len(set(words[k])))
