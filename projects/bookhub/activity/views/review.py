from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
from .permission import IsOwnerOrReadOnly

from ..serializers import ReviewBookSerializer, ReviewCreateSerializer, ReviewUpdateSerializer, ReviewUserSerializer
from ..models import Review


class ReviewApiView(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):

    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if (self.action == "list"):
            return ReviewUserSerializer
        if (self.action == "create"):
            return ReviewCreateSerializer
        if (self.action == "patch"):
            return ReviewUpdateSerializer
        return ReviewUserSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context
    
    def get_queryset(self):
        if (self.action in ["list", "retrieve"]):
            return Review.objects.all().select_related("book") 
        return super().get_queryset()
    
    def list(self, request, *args, **kwargs):
        """
        List of reviews for authenticated user
        """
        self.queryset = Review.objects.filter(user=request.user)
        return super().list(request, *args, **kwargs)
