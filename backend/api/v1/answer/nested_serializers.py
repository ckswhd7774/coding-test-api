from rest_framework import serializers

from app.explanation.models import Explanation


class AnswerExplanationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explanation
        fields = ["text"]
        read_only_fields = ["answer", "text"]
        ref_name = "AnswerExplanationSerializer"
