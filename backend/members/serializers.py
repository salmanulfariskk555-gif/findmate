from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Profile
def is_adult(value):
    today=date.today()
    years=today.year-value.year-((today.month,today.day)<(value.month,value.day))
    if years<18: raise serializers.ValidationError("FindMate is only for adults 18+.")
    if years>110: raise serializers.ValidationError("Enter a valid birth date.")
    return value
class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=150)
    password=serializers.CharField(write_only=True,validators=[validate_password])
    display_name=serializers.CharField(max_length=80)
    birth_date=serializers.DateField(validators=[is_adult])
    def validate_username(self,value):
        if User.objects.filter(username__iexact=value).exists(): raise serializers.ValidationError("Username unavailable.")
        return value
    def create(self,data):
        user=User.objects.create_user(username=data["username"],password=data["password"])
        Profile.objects.create(user=user,display_name=data["display_name"],birth_date=data["birth_date"])
        return user
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=["id","display_name","birth_date","city","bio","interests","visible","approved"]
        read_only_fields=["id","approved"]
    def validate_birth_date(self,value): return is_adult(value)
class PublicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=["id","display_name","city","bio","interests"]
