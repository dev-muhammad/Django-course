from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from ..serializers import GenreSerializer
from ..models import Genre


class GenreApiView(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):

    permission_classes = [IsAuthenticated,]
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
