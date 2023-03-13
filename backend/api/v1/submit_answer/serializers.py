from django.db import transaction
from rest_framework import serializers

from app.submit_answer.models import SubmitAnswer


class SubmitAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitAnswer
        fields = ["id", "user", "question", "is_correct", "text"]
        read_only_fields = ["id", "user", "is_correct"]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        instance = SubmitAnswer.objects.create(**validated_data, user_id=self.context["view"].kwargs["question_id"])
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
