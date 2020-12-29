from rest_framework.response import Response
from photos.models import Images, Albums
from photos.serializers import AlbumSerializer, ImageSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework import viewsets


class ImageView(viewsets.ModelViewSet):
    parser_class = [FileUploadParser]
    queryset = Images.objects.filter()
    serializer_class = ImageSerializer

    def get_queryset(self):
        queryset = self.queryset
        filtered_queryset = queryset.filter(user_id=self.request.user)
        return filtered_queryset

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        queryset = self.queryset
        filtered_queryset = queryset.get(user_id=request.user, id=params.get("pk"))
        serializer = self.serializer_class(filtered_queryset)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(
            user_id=self.request.user, image_file=self.request.data.get("image_file")
        )


class AlbumView(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Albums.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        filtered_queryset = queryset.filter(user_id=self.request.user)
        return filtered_queryset

    def perform_create(self, serializer):
        serializer.save(
            user_id=self.request.user, album_name=self.request.data.get("album_name")
        )

    def partial_update(self, request, pk=0):
        album_data = self.get_object()
        data = request.data
        album_data.images.set(data.get("image"))
        serializer = AlbumSerializer(album_data)
        return Response(serializer.data)
