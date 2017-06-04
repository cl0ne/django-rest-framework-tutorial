from django.contrib.auth import get_user_model
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlighted = serializers.ReadOnlyField()

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'highlighted', 'owner', 'linenos', 'language', 'style')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'snippets')
