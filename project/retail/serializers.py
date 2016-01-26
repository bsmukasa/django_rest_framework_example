from rest_framework import serializers

from project.retail.models import Chain, Store


class ChainSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    slogan = serializers.CharField(required=False, allow_blank=True, max_length=500)
    founded_date = serializers.DateField()
    website = serializers.URLField()

    def create(self, validated_data):
        """Create and return a new Chain instance given the validated data.

        :param validated_data: The validated data used to create a Chain instance.
        :return: Newly created Chain instance.
        """
        return Chain.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing Chain instance, given the validated data.

        :param instance: A Chain instance.
        :param validated_data: The validated data used to update a Chain instance.
        :return: Updated Chain instance.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.slogan = validated_data.get('slogan', instance.slogan)
        instance.founded_date = validated_data.get('founded_date', instance.founded_date)
        instance.website = validated_data.get('website', instance.website)
        instance.save()
        return instance


class StoreSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    number = serializers.CharField(required=False, allow_blank=True, max_length=20)
    address = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    opening_date = serializers.DateField()
    business_hours_start = serializers.IntegerField()
    business_hours_end = serializers.IntegerField()

    def create(self, validated_data):
        """Create and return a new Store instance given the validated data.

        :param validated_data: The validated data used to create a Store instance.
        :return: Newly created Store instance.
        """
        return Store.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing Store instance, given the validated data.

        :param instance: A Store instance.
        :param validated_data: The validated data used to update a Store instance.
        :return: Updated Store instance.
        """
        instance.number = validated_data.get('number', instance.number)
        instance.address = validated_data.get('address', instance.address)
        instance.opening_date = validated_data.get('opening_date', instance.opening_date)
        instance.business_hours_start = validated_data.get('business_hours_start', instance.business_hours_start)
        instance.business_hours_end = validated_data.get('business_hours_end', instance.business_hours_end)
