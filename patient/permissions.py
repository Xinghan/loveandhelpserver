from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
