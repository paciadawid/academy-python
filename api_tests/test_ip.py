import unittest
import requests


class TestIP(unittest.TestCase):
    def test_json_format(self):
        params = {
            "format": "json"
        }
        res = requests.get("https://api.ipify.org", params=params)
        # self.assertEqual("54.86.50.139" ,res.json()["ip"])
        self.assertEqual(dict, type(res.json()))
        self.assertEqual(200, res.status_code)
        self.assertRegex(res.json()["ip"], "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")

    def test_text_format(self):
        res = requests.get("https://api.ipify.org")
        self.assertTrue(res.text)


if __name__ == '__main__':
    unittest.main()
