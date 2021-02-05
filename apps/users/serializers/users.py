"""Users serializers."""

# Rest framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# JWT
import jwt

# Django
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from django.conf import settings

# Models
from apps.users.models import User

# Utilities
from datetime import timedelta

class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class"""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )


class UserSignupSerializer(serializers.Serializer):
    """Users sign up serializer. Handle users creation."""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all()
    )])

    username = serializers.CharField(
        min_length=4,
        max_length=50,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )

    picture = serializers.ImageField(required=False)

    password = serializers.CharField(min_length=8)
    password_confirmation = serializers.CharField(min_length=8)

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )

    phone_number = serializers.CharField(validators=[phone_regex])

    first_name = serializers.CharField(min_length=3, max_length=40)
    last_name = serializers.CharField(min_length=3, max_length=40)

    def validate(self, data):
        """Verify that passwords match."""

        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:
            raise serializers.ValidationError('Passowords do not match')
    
        password_validation.validate_password(passwd)
        return data

    def create(self, validated_data):
        """Create user with the requesting data."""
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(**validated_data, is_verified=False, is_client=True)
        self.send_confirmation_email(user)
        return user

    def send_confirmation_email(self, user):
        """Send account verification link to given user."""
        verification_token = self.gen_verication_token(user)
        
        subject = 'Welcome @{}! Verify your account to start using the app'.format(user.username)
        from_email = 'Contact List <noreply@contactlist.com>'
        text_content = render_to_string(
            'emails/account_verifiaction.html',
            {'token' : verification_token, 'user': user}
        )
        msg = EmailMultiAlternatives(subject, text_content, from_email, [user.email])
        msg.attach_alternative(text_content, "text/html")
        msg.send()

    def gen_verication_token(self, user):
        """Create JWT token that the user can use to verify its account."""
        exp_date = timezone.now() + timedelta(days=2)

        payload = {
            'user': user.username,
            'exp': int(exp_date.timestamp()),
            'type': 'email_confirmation'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        
        return token


class UserLoginSerializer(serializers.Serializer):
    """User Login Serializer. Handle login request data"""
    
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def validate(self, data):
        """Verify credentials."""
        user = authenticate(username=data['email'], password=data['password'])

        if not user:
            raise serializers.ValidationError('Invalid credentials')
        
        if not user.is_verified:
            raise serializers.ValidationError('Your account is not active yet :(')

        self.context['user'] = user
        return data


    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])

        return self.context['user'], token.key


class UserVerificationSerializer(serializers.Serializer):
    """Users verification serializer."""
    token = serializers.CharField()

    def validate_token(self, data):
        """Verify token is valid."""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid Token')

        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Invalid token type')
        
        self.context['payload'] = payload

        return data

    def save(self):
        """Update users verify status."""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()