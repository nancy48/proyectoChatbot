import json
from unittest import TestCase
from fastapi.testclient import TestClient
from main import app


class TestWebhook(TestCase):
    client = TestClient(app)

    def test_webhook_empty_request(self):
        response = self.client.post(url="/webhook", json={})
        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(
            json.loads(response.text),
            {
                "detail": [
                    {
                        "loc": ["body", "update_id"],
                        "msg": "field required",
                        "type": "value_error.missing",
                    },
                    {
                        "loc": ["body", "message"],
                        "msg": "field required",
                        "type": "value_error.missing",
                    },
                ]
            },
        )

    def test_webhook_empty_text(self):
        data = {
            "update_id": 56918934,
            "message": {
                "message_id": 86,
                "from": {
                    "id": 1084783282,
                    "is_bot": False,
                    "first_name": "faqn2",
                    "username": "faQn2s",
                    "language_code": "es",
                },
                "chat": {
                    "id": 1084783282,
                    "first_name": "faqn2",
                    "username": "faQn2s",
                    "type": "private",
                },
                "date": 1641925988,
                "text": "",
            },
        }

        response = self.client.post(url="/webhook", json=data)
        # TODO: ver este test con los chicos de Construyendo mi futuro

    def test_webhook_successful(self):
        data = {
            "update_id": 56918934,
            "message": {
                "message_id": 86,
                "from": {
                    "id": 1084783282,
                    "is_bot": False,
                    "first_name": "faqn2",
                    "username": "faQn2s",
                    "language_code": "es",
                },
                "chat": {
                    "id": 1084783282,
                    "first_name": "faqn2",
                    "username": "faQn2s",
                    "type": "private",
                },
                "date": 1641925988,
                "text": "Mensaje",
            },
        }

        response = self.client.post(url="/webhook", json=data)

        self.assertTrue(response.ok)
        self.assertEqual(response.text, "Message sent")
        self.assertEqual(response.status_code, 200)
