from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.answer.models import Answer
from app.submit_answer.models import SubmitAnswer
from app.submit_answer.tasks import grading


class SubmitAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitAnswer
        fields = ["id", "user", "question", "is_correct", "text", "status", "score", "created_at"]
        read_only_fields = ["id", "user", "is_correct", "status", "score", "created_at"]

    def validate(self, attrs):
        try:
            attrs["answer"] = Answer.objects.get(question_id=attrs["question"])
        except:
            raise ValidationError("해당 문제의 답이 등록되어 있지 않습니다.")
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        answer = validated_data.pop("answer")
        question = validated_data.pop("question")

        instance = SubmitAnswer.objects.create(
            **validated_data, user_id=self.context["request"].user.id, question_id=question.id, status=1
        )
        grading.delay(instance, answer)

        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
