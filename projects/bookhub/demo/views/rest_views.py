from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import BookSerializer
from ..models import Book


class BookApiView(APIView):

    queryset = Book.objects.all()

    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
