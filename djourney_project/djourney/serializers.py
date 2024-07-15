from rest_framework import serializers
from .models import City, Attraction, Review

class CitySerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        many=True,
        read_only=True
    )

    city_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'city_detail'
    )

    class Meta:
        model = City
        fields = ('id', 'city_url' ,'name', 'country', 'state', 'image_url', 'attraction')

class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.HyperlinkedRelatedField(
        view_name='city_detail',
        read_only=True
    )
    review = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True
    )
    city_url = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city'
    )
    class Meta:
        model = Attraction
        fields = ('id', 'city', 'city_url', 'name', 'demographic', 'description', 'review')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        read_only=True
    )
    class Meta:
        model=Review
        fields= ('id', 'reviewer_name', 'stars', 'description', 'attraction')