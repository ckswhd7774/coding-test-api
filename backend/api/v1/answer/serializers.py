from rest_framework import serializers

from api.v1.answer.nested_serializers import AnswerExplanationSerializer
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
        attrs = super().validate(attrs)
        return attrs

    def create(self, validated_data):
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
