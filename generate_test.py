import secrets
import unittest

import generate
from generate import MAX_LENGTH, MIN_LENGTH


class TestMain(unittest.TestCase):
    def test_invalid_input(self):
        output = generate.main(["asdf"])
        self.assertEqual(1, len(output["items"]))
        self.assertFalse(output["items"][0]["valid"])

    def test_default_length(self):
        output = generate.main([])
        self.assertEqual(16, len(output["items"][0]["title"]))
        self.assertEqual(16, len(output["items"][0]["arg"]))


class TestGenerate(unittest.TestCase):
    def test_length(self):
        password = generate.generate(20)
        self.assertEqual(20, len(password))

    def test_generate_complexity(self):
        for i in range(0, 10):
            password = generate.generate(20)
            self.assertRegex(password, ".*[0-9]+.*")
            self.assertRegex(password, r".*[!@#$%^&*()\-_=+\"',./\\:;{}~|]+.*")

    def test_no_dupes(self):
        passwords = []
        for i in range(0, 10000):
            length = secrets.randbelow(MAX_LENGTH - MIN_LENGTH) + MIN_LENGTH + 1
            password = generate.generate(length)
            passwords.append(password)
            self.assertEqual(length, len(password))

        self.assertEqual(len(passwords), len(set(passwords)))
