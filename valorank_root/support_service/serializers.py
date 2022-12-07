from rest_framework import serializers
from .models import Request


class SupportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('email', 'problem_description', 'creation_time')