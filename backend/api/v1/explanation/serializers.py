from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import serializers

from app.explanation.models import Explanation
from app.question.models import Question


class ExplanationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explanation
        fields = ["id", "text"]

    def validate(self, attrs):
        if not attrs["text"]:
            raise ValidationError("해설을 적어주세요")

        if not Question.objects.get(id=self.context["view"].kwargs["question_id"]).user == self.context["request"].user:
            raise ValidationError("문제를 만든 유저만 헤설을 등록할 수 있습니다.")

        if Explanation.objects.filter(question_id=self.context["view"].kwargs["question_id"]).exists():
            raise ValidationError("이미 해당 문제의 해설이 존재합니다.")
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        instance = Explanation.objects.create(**validated_data, question_id=self.context["view"].kwargs["question_id"])
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
