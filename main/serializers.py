from rest_framework import serializers
from .models import JobAdvert, JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobApplication
        fields = "__all__"
        
        
class JobAdvertSerializer(serializers.ModelSerializer):
    applications = JobApplicationSerializer(many=True, read_only=True)
    
    class Meta:
        model = JobAdvert
        fields = '__all__'