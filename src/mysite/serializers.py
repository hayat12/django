from rest_framework.serializers import ModelSerializer
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from mysite.models import Person, File
from django.contrib.auth.models import User

# Serializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'url'
        )


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name'
        )


class FileSerializer(ModelSerializer):
    class Meta():
        model = File
        fields = ('file', 'remark', 'timestamp')

class ResgisterSerializer(ModelSerializer):
    class Meta():
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')