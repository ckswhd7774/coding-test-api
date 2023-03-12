from rest_framework import serializers

from app.explanation.models import Explanation


class ExplantaionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explanation
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
