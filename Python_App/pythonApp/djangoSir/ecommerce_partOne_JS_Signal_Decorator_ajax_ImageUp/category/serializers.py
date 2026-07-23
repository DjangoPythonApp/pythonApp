import re

from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    

    name = serializers.CharField(
        error_messages={
            "blank": "Category name cannot be given blank."
        }
    )

    description = serializers.CharField(
        error_messages={
            "blank": "Description cannot be empty."
        }
    )

    class Meta:
        model = Category
        fields = "__all__"

    def validate_name(self, value):
        value = value.strip()

        pattern = r'^[A-Za-z][A-Za-z0-9 ]{2,49}$'

        if not re.fullmatch(pattern, value):
            raise serializers.ValidationError(
                "Category name must start with a letter and contain only letters, numbers and spaces."
            )

        return value

    def validate_description(self, value):
        value = value.strip()

        pattern = r'^[A-Za-z0-9\s.,]{10,500}$'

        if not re.fullmatch(pattern, value):
            raise serializers.ValidationError(
                "Description must be between 10 and 500 characters and contain only letters, numbers, spaces, commas and periods."
            )

        return value