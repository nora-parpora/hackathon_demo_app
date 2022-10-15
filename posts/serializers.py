from rest_framework import serializers

from posts.models import JobAdvert

class JobAdvertSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobAdvert
        fields = ["position", "city", "sector", "description", "employment_type"]

    def set_employer(self, employer):
        self.employer = employer

    def create(self, validated_data):

        jobad = JobAdvert.objects.create(position=validated_data['position'],
                                        city=validated_data['city'],
                                        sector=validated_data['sector'],
                                        description=validated_data['description'],
                                        employment_type=validated_data['employment_type'],
                                        employer=self.employer,
                                         )

        jobad.save()
        return jobad