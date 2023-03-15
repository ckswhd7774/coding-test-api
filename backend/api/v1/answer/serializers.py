from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.answer.models import Answer


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
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        instance = super().create(validated_data)
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
