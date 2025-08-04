from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from vinyl.application.usecases import AlbumService
from vinyl.api.serializers import AlbumSerializer

class AlbumCreateView(APIView):

    """
    View to create a new album.
    """
    def create_album(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():

            try:
                album = AlbumService.create_album(serializer.validated_data)
                return Response(AlbumSerializer(album).data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)