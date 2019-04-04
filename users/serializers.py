from rest_framework import serializers
from users.models import User
from .utils import is_email_valid, user_enrichment


class UserCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        write_only_fields = ('password', )

    # def __init__(self, *args, **kwargs):
    #     super(UserCreationSerializer, self).__init__(*args, **kwargs)

    def validate_username(self, username):
        return username.lower()

    def validate_email(self, email):
        email = email.lower()
        if is_email_valid(email):
            return email

        raise serializers.ValidationError(
            "A fake email address was detected, use another one")

    def create(self, validated_data):
        additional_data = user_enrichment(validated_data.get('email'))
        return User.objects.create_user(**validated_data, **additional_data)