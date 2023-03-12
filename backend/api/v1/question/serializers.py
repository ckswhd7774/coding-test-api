from rest_framework import serializers

from app.question.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display")
    
    class Meta:
        model = Question
        fields = [
            "id",
            "type",
            "title",
            "text",
            "restrictions"
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
