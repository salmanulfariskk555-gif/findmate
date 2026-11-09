from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from dating.models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    date_of_birth = serializers.DateField(write_only=True)
    class Meta:
        model = User
        fields = ('id','username','email','password','date_of_birth')
    def validate_email(self, value):
        value = value.lower().strip()
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('An account with this email already exists.')
        return value
    def validate_date_of_birth(self, value):
        from datetime import date
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 18:
            raise serializers.ValidationError('FindMate is available to adults aged 18 and above only.')
        return value
    def create(self, validated_data):
        dob = validated_data.pop('date_of_birth')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, date_of_birth=dob)
        return user

class MeSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id','username','email','profile')
        read_only_fields = fields
    def get_profile(self, obj):
        from dating.serializers import ProfileSerializer
        try:
            return ProfileSerializer(obj.profile, context=self.context).data
        except Profile.DoesNotExist:
            return None
