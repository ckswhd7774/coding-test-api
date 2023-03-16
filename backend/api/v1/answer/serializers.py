from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.answer.models import Answer
from app.question.models import Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            "id",
            "question",
            "text",
        ]
        read_only_fields = ["id", "question"]

    def validate(self, attrs):
        if not attrs["text"]:
            raise ValidationError("답을 적어주세요")

        if not Question.objects.get(id=self.context["view"].kwargs["question_id"]).user == self.context["request"].user:
            raise ValidationError("문제를 만든 유저만 답을 등록할 수 있습니다.")

        if Answer.objects.filter(question_id=self.context["view"].kwargs["question_id"]).exists():
            raise ValidationError("이미 해당 문제의 답이 존재합니다.")
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        instance = Answer.objects.create(**validated_data, question_id=self.context["view"].kwargs["question_id"])
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
