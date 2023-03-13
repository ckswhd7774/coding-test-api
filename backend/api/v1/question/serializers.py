from rest_framework import serializers

from api.v1.question.nested_serializers import QuestionExplanationSerializer, QuestionSubmitAnswerSerializer
from app.question.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.get_name_display")
    is_submitted = serializers.BooleanField(read_only=True)
    explanation = QuestionExplanationSerializer(read_only=True)
    submitanswer_set = QuestionSubmitAnswerSerializer(read_only=True, many=True)
    score_avg = serializers.FloatField(read_only=True)

    class Meta:
        model = Question
        fields = [
            "id",
            "category",
            "title",
            "text",
            "restrictions",
            "is_submitted",
            "explanation",
            "submitanswer_set",
            "score_avg",
        ]
        read_only_fields = ["id"]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        return attrs

    def create(self, validated_data):
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
