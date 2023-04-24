import unittest
import requests
from faker import Faker
from src.gorest_handler import APIHandler


class GorestTest(unittest.TestCase):

    def setUp(self) -> None:
        self.api_handler = APIHandler()

    def test_create_user(self):
        body = {
            "name": Faker().name(),
            "gender": "male",
            "email": Faker().email(),
            "status": "active"
        }
        res_body = self.api_handler.create_user(body)
        self.assertEqual(int, type(res_body["id"]))
        self.assertDictContainsSubset(body, res_body)


if __name__ == '__main__':
    unittest.main()
