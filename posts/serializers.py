from rest_framework import serializers

from posts.models import JobAdvert, RentAdvert


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


class RentAdvertSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentAdvert
        fields = ["rental_type", "city", "rooms", "rent", "description"]

    def set_owner(self, owner):
        self.owner = owner

    def create(self, validated_data):

        rented = RentAdvert.objects.create(rental_type=validated_data['rental_type'],
                                        city=validated_data['city'],
                                        rooms=validated_data['rooms'],
                                        rent=validated_data['rent'],
                                        description=validated_data['description'],
                                        owner=self.owner,
                                         )

        rented.save()
        return rented