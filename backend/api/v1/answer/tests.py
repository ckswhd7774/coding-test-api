import random

from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from app.answer.models import Answer
from app.question.models import Question
from app.user.models import User

faker = Faker(locale="ko_KR")


class AnswerListAPITest(APITestCase):
    """
    - 성공 상태 코드 테스트
    - 페이지네이션 응답 필드 테스트
    - 페이지네이션 사이즈 테스트
    - 성공 응답 필드 테스트
    """

    MODEL = Answer
    METHOD = "get"
    PATH = "/v1/question/{question_id}/answer/"
    PAGINATED_RESPONSE_FIELDS = ["cursor", "results"]
    PAGINATION_DEFAULT_PAGE_SIZE = 20

    SUCCESS_STATUS_CODE = status.HTTP_200_OK
    SUCCESS_RESPONSE_FIELDS = ["id", "question", "text"]  # TODO: add success response fields

    @classmethod
    def create_test_data(cls):
        question_data_set = [
            Question(
                id=i + 1,
                category_id=random.randint(1, 2),
                title=faker.text(max_nb_chars=10),
                text=faker.text(max_nb_chars=100),
                restrictions=faker.text(max_nb_chars=10),
                level=random.randint(1, 3),
                score=random.randint(0, 100),
                submit_count=random.randint(1, 100),
            )
            for i in range(0, 25)
        ]

        data_set = [
            {
                "id": i + 1,
                "question_id": i + 1,
                "text": faker.text(max_nb_chars=100),
            }
            for i in range(0, 25)
        ]
        Question.objects.bulk_create(question_data_set)
        cls.MODEL.objects.bulk_create([cls.MODEL(**data) for data in data_set])

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(email="test@test.com")
        cls.create_test_data()

    def setUp(self):
        self.client.force_authenticate(User.objects.get(email="test@test.com"))

    def test_success_response(self):
        response = getattr(self.client, self.METHOD)(self.PATH)

        # 성공 상태 코드 테스트
        self.assertEqual(
            self.SUCCESS_STATUS_CODE,
            response.status_code,
            f"{self.__class__.__name__} 성공 상태 코드 테스트 실패",
        )
        # 페이지네이션 응답 필드 테스트
        self.assertListEqual(
            sorted(self.PAGINATED_RESPONSE_FIELDS),
            sorted(response.data.keys()),
            f"{self.__class__.__name__} 페이지네이션 응답 테스트 실패",
        )
        # 페이지네이션 사이즈 테스트
        self.assertTrue(
            self.PAGINATION_DEFAULT_PAGE_SIZE >= len(response.data["results"]),
            f"{self.__class__.__name__} 페이지네이션 사이즈 테스트 실패",
        )
        # 성공 응답 필드 테스트
        for data in response.data["results"]:
            self.assertListEqual(
                sorted(self.SUCCESS_RESPONSE_FIELDS),
                sorted(list(data)),
                f"{self.__class__.__name__} 성공 응답 필드 테스트 실패",
            )


class AnswerCreateAPITest(APITestCase):
    """
    - 성공 상태 코드 테스트
    - 성공 응답 필드 테스트
    - 생성된 데이터 테스트
    - 실패 상태 코드 테스트
    - 실패 응답 필드 테스트
    """

    MODEL = Answer
    METHOD = "post"
    PATH = "/v1/answer/"

    SUCCESS_STATUS_CODE = status.HTTP_201_CREATED
    SUCCESS_DATA_SET = [
        {
            "request": {},  # TODO: add success request data set
            "response": {"id": 1},  # TODO: add success response data set
            "instance": {"id": 1},  # TODO: add success instance data set
        },
    ]

    FAILURE_STATUS_CODE = status.HTTP_400_BAD_REQUEST
    FAILURE_DATA_SET = [
        # {
        #     "request": {},  # TODO: add failure request data set
        #     "response": {},  # TODO: add failure response data set
        # },
    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(email="test@test.com")

    def setUp(self):
        self.client.force_authenticate(User.objects.get(email="test@test.com"))

    def test_success_response(self):
        for success_data in self.SUCCESS_DATA_SET:
            response = getattr(self.client, self.METHOD)(self.PATH, data=success_data["request"])

            # 성공 상태 코드 테스트
            self.assertEqual(
                self.SUCCESS_STATUS_CODE,
                response.status_code,
                f"{self.__class__.__name__} 성공 상태 코드 테스트 실패",
            )
            # 성공 응답 테스트
            self.assertDictEqual(
                success_data["response"],
                response.data,
                f"{self.__class__.__name__} 성공 응답 테스트 실패",
            )
            # 생성된 데이터 테스트
            instance = self.MODEL.objects.get(id=response.data["id"])
            for attr, value in success_data["instance"].items():
                self.assertEqual(value, getattr(instance, attr), f"{self.__class__.__name__} 생성된 데이터 테스트 실패")

    def test_failure_response(self):
        for failure_data in self.FAILURE_DATA_SET:
            response = getattr(self.client, self.METHOD)(self.PATH, data=failure_data["request"])

            # 실패 상태 코드 테스트
            self.assertEqual(
                self.FAILURE_STATUS_CODE,
                response.status_code,
                f"{self.__class__.__name__} 실패 상태 코드 테스트 실패",
            )
            # 실패 응답 테스트
            self.assertDictEqual(
                failure_data["response"],
                response.data,
                f"{self.__class__.__name__} 실패 응답 테스트 실패",
            )


class AnswerRetrieveAPITest(APITestCase):
    """
    - 성공 상태 코드 테스트
    - 성공 응답 테스트
    """

    MODEL = Answer
    METHOD = "get"
    PATH = "/v1/answer/{id}/"

    SUCCESS_STATUS_CODE = status.HTTP_200_OK
    SUCCESS_RESPONSE_DATA = {"id": 1}  # TODO: add success response data

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


class AnswerUpdateAPITest(APITestCase):
    """
    - 성공 상태 코드 테스트
    - 성공 응답 테스트
    - 수정된 데이터 테스트
    - 실패 상태 코드 테스트
    - 실패 응답 테스트
    """

    MODEL = Answer
    METHOD = "put"
    PATH = "/v1/answer/{id}/"

    SUCCESS_STATUS_CODE = status.HTTP_200_OK
    SUCCESS_DATA_SET = [
        {
            "request": {},  # TODO: add success request data set
            "response": {"id": 1},  # TODO: add success response data set
            "instance": {"id": 1},  # TODO: add success instance data set
        },
    ]

    FAILURE_STATUS_CODE = status.HTTP_400_BAD_REQUEST
    FAILURE_DATA_SET = [
        # {
        #     "request": {},  # TODO: add failure request data set
        #     "response": {},  # TODO: add failure response data set
        # },
    ]

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
        for success_data in self.SUCCESS_DATA_SET:
            response = getattr(self.client, self.METHOD)(
                self.PATH.format(id=self.instance.id), data=success_data["request"]
            )

            # 성공 상태 코드 테스트
            self.assertEqual(
                self.SUCCESS_STATUS_CODE,
                response.status_code,
                f"{self.__class__.__name__} 성공 상태 코드 테스트 실패",
            )
            # 성공 응답 테스트
            self.assertDictEqual(
                success_data["response"],
                response.data,
                f"{self.__class__.__name__} 성공 응답 테스트 실패",
            )
            # 생성된 데이터 테스트
            instance = self.MODEL.objects.get(id=response.data["id"])
            for attr, value in success_data["instance"].items():
                self.assertEqual(value, getattr(instance, attr), f"{self.__class__.__name__} 생성된 데이터 테스트 실패")

    def test_failure_response(self):
        for failure_data in self.FAILURE_DATA_SET:
            response = getattr(self.client, self.METHOD)(
                self.PATH.format(id=self.instance.id), data=failure_data["request"]
            )

            # 실패 상태 코드 테스트
            self.assertEqual(
                self.FAILURE_STATUS_CODE,
                response.status_code,
                f"{self.__class__.__name__} 실패 상태 코드 테스트 실패",
            )
            # 실패 응답 테스트
            self.assertDictEqual(
                failure_data["response"],
                response.data,
                f"{self.__class__.__name__} 실패 응답 테스트 실패",
            )


class AnswerDestroyAPITest(APITestCase):
    """
    - 성공 상태 코드 테스트
    - 삭제된 데이터 테스트
    """

    MODEL = Answer
    METHOD = "delete"
    PATH = "/v1/answer/{id}/"

    SUCCESS_STATUS_CODE = status.HTTP_204_NO_CONTENT

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
        # 삭제된 데이터 테스트
        self.assertFalse(
            self.MODEL.objects.filter(id=self.instance.id).exists(),
            f"{self.__class__.__name__} 삭제된 데이터 테스트 실패",
        )
