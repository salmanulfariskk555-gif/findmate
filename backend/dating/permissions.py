from rest_framework.permissions import BasePermission
from .models import Match

class IsMatchParticipant(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.match.user_one_id == user.id or obj.match.user_two_id == user.id
