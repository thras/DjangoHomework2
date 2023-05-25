from rest_framework import serializers
from jobs.models import JobOffer

class JobsSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobOffer
        fields = "__all__"

    def validate(self, data):
        if data["job_title"] == data["job_description"]:
            raise serializers.ValidationError("Title and description should be different")
        return data
    
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title should contain more then 3 chars")
        return value