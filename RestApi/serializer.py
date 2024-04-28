from rest_framework import serializers
from django import forms


class listSerialize(serializers.Serializer):
    title = serializers.CharField(max_length=122)
    description = serializers.CharField(max_length=122)
    created_at = serializers.DateField()
    completed = serializers.DateField()

