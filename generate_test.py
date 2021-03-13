import unittest

import generate


class TestMain(unittest.TestCase):
    def test_invalid_input(self):
        output = generate.main(["asdf"])
        self.assertEqual(1, len(output["items"]))
        self.assertFalse(output["items"][0]["valid"])

    def test_default_length(self):
        output = generate.main([])
        self.assertEqual(15, len(output["items"][0]["title"]))
        self.assertEqual(15, len(output["items"][0]["arg"]))


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
        for i in range(0, 1000):
            passwords.append(generate.generate(15))

        self.assertEqual(len(passwords), len(set(passwords)))
