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

    # def test_e2e_flow(self):
    #     self.api_handler.create_user()
    #     self.api_handler.get_user_by_id()
    #     self.api_handler.update_user()
    #     self.api_handler.get_user_by_id()
    #     self.api_handler.delete_user()
    #     self.api_handler.get_user_by_id()

    def test_add_delete_post(self):
        user_id = self.api_handler.create_user(random_user=True)["id"]
        post_body = {
            "title": Faker().sentence(),
            "body": Faker().paragraph()
        }
        post_id = self.api_handler.create_post(user_id, post_body)["id"]
        user_post = self.api_handler.get_post(post_id)
        self.assertTrue(user_post)
        self.api_handler.delete_post(post_id)
        self.api_handler.get_post(post_id, expected_status_code=404)

    def test_create_post_without_body(self):
        user_id = self.api_handler.create_user(random_user=True)["id"]
        post_body = {
            "title": Faker().sentence()
        }
        res_body = self.api_handler.create_post(user_id, post_body, expected_status_code=422)
        self.assertEqual("body", res_body[0]["field"])

if __name__ == '__main__':
    unittest.main()
