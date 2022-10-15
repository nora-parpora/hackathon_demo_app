from rest_framework import serializers

from accounts.models import Employer
from accounts.serializers import EmployerSerializer
from posts.models import JobAdvert

from rest_framework_simplejwt.tokens import AccessToken

class JobAdvertSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobAdvert
        fields = ["position", "city", "sector", "description", "employment_type"]

    def set_employer(self, empl_id):
        self.empl_id = empl_id

    def create(self, validated_data):

        e = Employer.objects.all().get(pk=self.empl_id)


        jobad = JobAdvert.objects.create(position=validated_data['position'],
                                        city=validated_data['city'],
                                        sector=validated_data['sector'],
                                        description=validated_data['description'],
                                        employment_type=validated_data['employment_type'],
                                        employer=e,
                                         )

        jobad.save()
        return jobad