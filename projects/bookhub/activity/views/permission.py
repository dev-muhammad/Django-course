from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.IsAuthenticated):
    """
    Custom permission to only allow the owner of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        # Write permissions are only allowed to the owner of the object.
        return bool(request.user and request.user.is_authenticated and obj.user == request.user)
            
