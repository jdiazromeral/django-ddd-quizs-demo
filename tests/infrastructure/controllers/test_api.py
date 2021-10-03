from django.urls import reverse
from rest_framework.test import APITestCase, APIClient


class TestAPI(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.create_url = reverse("create")
        self.find_all = reverse("all")

    def test_get(self):
        response = self.client.get(self.find_all)
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.data)

        response = self.client.post(
            self.create_url,
            data="""
            {
                "id": "d8a13304-d815-4db4-b801-efb3f91d55f3",
                "title": "test title",
                "description": "test description",
                "type": "test type",
                "time": 10,
                "questions": [
                    {
                        "id": "a201429b-35d9-469c-9af1-125359d7d76e",
                        "text": "text question",
                        "skill": "LISTENING",
                        "answers": [
                            {
                                "id": "ff83bc63-cd97-453a-b9b1-287522ad00b1",
                                "text": "answer text",
                                "question_id": "a201429b-35d9-469c-9af1-125359d7d76e"
                            },
                            {
                                "id": "f099b566-7615-40a8-8a7b-1f5c174083c1",
                                "text": "answer text",
                                "question_id": "a201429b-35d9-469c-9af1-125359d7d76e"
                            }
                        ],
                        "correct_answer": ["ff83bc63-cd97-453a-b9b1-287522ad00b1"],
                        "quiz_id": "d8a13304-d815-4db4-b801-efb3f91d55f3"
                    }
                ]
            }
            """,
            content_type="application/json",
        )
        self.assertEqual(200, response.status_code)

        response = self.client.get(self.find_all)
        self.assertEqual(200, response.status_code)
        expected = [
            {
                "id": "d8a13304-d815-4db4-b801-efb3f91d55f3",
                "title": "test title",
                "description": "test description",
                "type": "test type",
                "time": 10,
                "questions": [
                    {
                        "id": "a201429b-35d9-469c-9af1-125359d7d76e",
                        "text": "text question",
                        "skill": "LISTENING",
                        "answers": {
                            "ff83bc63-cd97-453a-b9b1-287522ad00b1": {
                                "id": "ff83bc63-cd97-453a-b9b1-287522ad00b1",
                                "text": "answer text",
                                "question_id": "a201429b-35d9-469c-9af1-125359d7d76e",
                            },
                            "f099b566-7615-40a8-8a7b-1f5c174083c1": {
                                "id": "f099b566-7615-40a8-8a7b-1f5c174083c1",
                                "text": "answer text",
                                "question_id": "a201429b-35d9-469c-9af1-125359d7d76e",
                            },
                        },
                        "correct_answer": ["ff83bc63-cd97-453a-b9b1-287522ad00b1"],
                        "quiz_id": "d8a13304-d815-4db4-b801-efb3f91d55f3",
                    }
                ],
            }
        ]
        self.assertEqual(expected, response.data)
