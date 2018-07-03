from rest_framework import serializers
from student.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = fields=['student_id']
