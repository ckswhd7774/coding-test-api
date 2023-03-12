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

    def create(self, validated_data):
        instance = SubmitAnswer.objects.create(**validated_data, user_id=self.context["request"].user.id)
        return instance
