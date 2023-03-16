from rest_framework import serializers

from app.answer.models import Answer
from app.explanation.models import Explanation
from app.question.models import QuestionCategory
from app.submit_answer.models import SubmitAnswer


class QuestionExplanationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explanation
        fields = ["question", "text"]
        read_only_fields = ["question", "text"]
        ref_name = "QuestionExplanationSerializer"


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["text"]
        read_only_fields = ["text"]
        ref_name = "QuestionAnswerSerializer"


class QuestionSubmitAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitAnswer
        fields = ["id", "text", "is_correct", "score", "status"]
        read_only_fields = ["id", "text", "is_correct", "score", "status"]
        ref_name = "QuestionSubmitAnswerSerializer"
