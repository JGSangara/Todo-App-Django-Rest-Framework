from rest_framework import serializers
from tasks.models import Task
from accounts.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        email = data.get('email', '')
        password = data.get('password', '')

        if email and password:
            user = User.objects.filter(email=email).first()
            if user:
                if user.check_password(password):
                    data['user'] = user
                else:
                    raise serializers.ValidationError("Incorrect Password")
            else:
                raise serializers.ValidationError("User does not exist")
        else:
            raise serializers.ValidationError("Please provide email and password")
        return data


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'},  max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        password2 = data.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Passwords must match")
        return data

    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)