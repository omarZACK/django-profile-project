from rest_framework import permissions

class UpdateOwnProfiles(permissions.BasePermission):
    """Allows users to update their own profiles"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allows users to update their own status"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
