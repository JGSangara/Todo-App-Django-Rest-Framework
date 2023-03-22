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


