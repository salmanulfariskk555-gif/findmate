from rest_framework import serializers
from .models import Profile, Message, Report

class ProfileSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ('id','display_name','date_of_birth','age','gender','interested_in','city','bio','interests','photo_url','is_verified','is_visible')
        read_only_fields = ('id','age','is_verified')
    def get_age(self, obj):
        from datetime import date
        today = date.today(); dob = obj.date_of_birth
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    def validate_date_of_birth(self, value):
        from datetime import date
        today=date.today(); age=today.year-value.year-((today.month,today.day)<(value.month,value.day))
        if age < 18: raise serializers.ValidationError('Users must be 18 or older.')
        return value

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id','sender','body','created_at','is_read')
        read_only_fields = ('id','sender','created_at','is_read')

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('reported_user','reason','details')
