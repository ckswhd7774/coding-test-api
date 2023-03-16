from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.v1.question.nested_serializers import (
    QuestionAnswerSerializer,
    QuestionExplanationSerializer,
    QuestionSubmitAnswerSerializer,
)
from app.question.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.name", read_only=True)
    is_submitted = serializers.BooleanField(read_only=True)
    score_avg = serializers.FloatField(read_only=True)
    is_bookmarked = serializers.BooleanField(read_only=True)
    explanation = QuestionExplanationSerializer(read_only=True)
    submitanswer_set = QuestionSubmitAnswerSerializer(read_only=True, many=True)
    answer = QuestionAnswerSerializer(read_only=True)

    class Meta:
        model = Question
        fields = [
            "id",
            "category",
            "title",
            "text",
            "restrictions",
            "user",
            "level",
            "score",
            "submit_count",
            "is_submitted",
            "score_avg",
            "is_bookmarked",
            "explanation",
            "submitanswer_set",
            "answer",
        ]
        read_only_fields = ["id", "submit_count", "score"]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        instance = Question.objects.create(**validated_data, user=self.context["request"].user)
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        if not Question.objects.get(id=self.context['view'].kwargs['question_id']).user == self.context['request'].user:
            raise ValidationError('문제를 생성한 유저만 수정이 가능합니다.')
        instance = super().update(instance, validated_data)
        return instance
