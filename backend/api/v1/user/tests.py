from rest_framework import status
from rest_framework.test import APITestCase

from app.user.models import User


class UserLoginAPITest(APITestCase):
    METHOD = "post"
    PATH = "/v1/user/login/"
    RESPONSE_FIELDS = ["Token"]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(email="admin@admin.com", password="12")

    def test_login_success_response(self):
        response = getattr(self.client, self.METHOD)(self.PATH, data={"email": "admin@admin.com", "password": "12"})

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        # 응답 필드 테스트
        self.assertListEqual(
            sorted(self.RESPONSE_FIELDS),
            sorted(response.data.keys()),
            f"{self.__class__.__name__} 응답 필드 테스트 실패",
        )

    def test_login_failure_response_from_invalid_email(self):
        response = getattr(self.client, self.METHOD)(self.PATH, data={"email": "test2@test.com", "password": "12"})

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(
            {
                "email": ["인증정보가 일치하지 않습니다."],
                "password": ["인증정보가 일치하지 않습니다."],
                "non_field": ["없는 유저이거나 잘못된 비밀번호입니다."],
            },
            response.data,
        )

    def test_login_failure_response_from_invalid_password(self):
        response = getattr(self.client, self.METHOD)(self.PATH, data={"email": "admin@admin.com", "password": "12!"})

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(
            {
                "email": ["인증정보가 일치하지 않습니다."],
                "password": ["인증정보가 일치하지 않습니다."],
            },
            response.data,
        )


class UserLogoutAPITest(APITestCase):
    METHOD = "post"
    PATH = "/v1/user/logout/"

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(email="admin@admin.com", password="12")
        Device.objects.create(user=user, uid="uid", token="token")

    def setUp(self):
        self.user = User.objects.get(email="admin@admin.com")
        self.client.force_authenticate(self.user)

    def test_logout_success_response(self):
        response = getattr(self.client, self.METHOD)(self.PATH)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual({}, response.data)

    def test_logout_success_response_together_uid(self):
        response = getattr(self.client, self.METHOD)(self.PATH, data={"uid": "uid"})

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertFalse(self.user.device_set.filter(uid="uid").exists())
        self.assertEqual({}, response.data)


class UserMeAPITest(APITestCase):
    """
    - 성공 상태 코드 테스트
    - 성공 응답 테스트
    """

    MODEL = User
    METHOD = "get"
    PATH = "/v1/user/me/"

    SUCCESS_STATUS_CODE = status.HTTP_200_OK
    SUCCESS_RESPONSE_DATA = [
        {
            "id": 1,
            "username": "test",
            "nickname": "test",
            "email": "test@test.com",
            "phone": "01012341234",
            "birth_date": "",
            "role": "UA",
            "parent": "2",
        }
    ]  # TODO: add success response data

    @classmethod
    def create_test_data(cls):
        data = {}  # TODO: add test data
        cls.instance = cls.MODEL.objects.create(**data)

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(email="test@test.com")
        cls.create_test_data()

    def setUp(self):
        self.client.force_authenticate(User.objects.get(email="test@test.com"))

    def test_success_response(self):
        response = getattr(self.client, self.METHOD)(self.PATH.format(id=self.instance.id))

        # 성공 상태 코드 테스트
        self.assertEqual(
            self.SUCCESS_STATUS_CODE,
            response.status_code,
            f"{self.__class__.__name__} 성공 상태 코드 테스트 실패",
        )
        # 성공 응답 테스트
        self.assertDictEqual(
            self.SUCCESS_RESPONSE_DATA,
            response.data,
            f"{self.__class__.__name__} 성공 응답 필드 테스트 실패",
        )
