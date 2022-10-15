from rest_framework import serializers

from accounts.models import Profile, MyBaseUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBaseUser
        fields = ['email', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', "first_name", "last_name", "phone" or None]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        u = MyBaseUser.objects.create(**user_data)

        profile = Profile.objects.create(first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        phone=validated_data['phone'] or "",
                                        user=u,
                                         )
        u.set_password(user_data['password'])
        u.save()
        profile.save()
        return profile

