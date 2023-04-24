import unittest
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
        res_body = self.api_handler.get_user_by_id(res_body["id"])
        self.assertDictContainsSubset(body, res_body)

    def test_invalid_user_creation(self):
        body = {
            "name": Faker().name(),
            "gender": "male",
            "email": Faker().name(),
            "status": "active"
        }
        self.api_handler.create_user(body, expected_status_code=422)

if __name__ == '__main__':
    unittest.main()
