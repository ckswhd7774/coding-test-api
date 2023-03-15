from rest_framework import serializers

from app.mock_test_paper.models import MockTestPaper


class MockTestPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockTestPaper
        fields = [
            "id",
        ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        return attrs

    def create(self, validated_data):
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
