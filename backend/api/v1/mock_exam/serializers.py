from django.db import transaction
from rest_framework import serializers

from app.mock_exam.models import MockExam


class MockExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockExam
        fields = [
            "id",
        ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        instance = super().create(validated_data)
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
