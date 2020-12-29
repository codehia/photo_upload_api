from rest_framework import serializers
from photos.models import Albums, Images


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.SlugRelatedField(read_only=True, slug_field="id")

    class Meta:
        model = Images
        fields = ("id", "user_id", "image_file", "created_date")


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = ("id", "album_name", "images")
        depth = 1

