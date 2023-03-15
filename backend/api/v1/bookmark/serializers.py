from django.db import transaction
from rest_framework import serializers

from app.bookmark.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source="question.title")

    class Meta:
        model = Bookmark
        fields = ["id", "user", "question"]
        read_only_fields = ["id", "user"]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        instance = Bookmark.objects.create(user_id=self.context["request"].id, question_id=validated_data["question"])
        return instance
