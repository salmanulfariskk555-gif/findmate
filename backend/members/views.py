from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import Profile, Like, Block, Report
from .serializers import RegisterSerializer, ProfileSerializer, PublicProfileSerializer

def blocked_ids(user):
    return set(Block.objects.filter(blocker=user).values_list("blocked_id", flat=True)) | set(Block.objects.filter(blocked=user).values_list("blocker_id", flat=True))

def eligible(user, target):
    return target.pk != user.pk and target.pk not in blocked_ids(user) and Profile.objects.filter(user=target, visible=True, approved=True).exists()

class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "message": "Account created. Profile is hidden until approved."}, status=status.HTTP_201_CREATED)

class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

class DeleteAccountView(APIView):
    def delete(self, request):
        password = request.data.get("password", "")
        if not isinstance(password, str) or not request.user.check_password(password):
            return Response({"detail": "Correct password required to delete the account."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DiscoverView(generics.ListAPIView):
    serializer_class = PublicProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(visible=True, approved=True).exclude(user=self.request.user).exclude(user_id__in=blocked_ids(self.request.user)).order_by("-created_at")[:50]

class LikeView(APIView):
    def post(self, request, pk):
        try:
            target = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)
        if not eligible(request.user, target):
            return Response({"detail": "Profile unavailable."}, status=400)
        Like.objects.get_or_create(sender=request.user, recipient=target)
        mutual = Like.objects.filter(sender=target, recipient=request.user).exists()
        return Response({"matched": mutual})

class MatchesView(APIView):
    def get(self, request):
        sent = Like.objects.filter(sender=request.user).values_list("recipient_id", flat=True)
        received = Like.objects.filter(recipient=request.user).values_list("sender_id", flat=True)
        ids = set(sent) & set(received)
        profiles = Profile.objects.filter(user_id__in=ids, visible=True, approved=True).exclude(user_id__in=blocked_ids(request.user))
        return Response(PublicProfileSerializer(profiles, many=True).data)

class BlockView(APIView):
    def post(self, request, pk):
        if pk == request.user.pk:
            return Response({"detail": "Cannot block yourself."}, status=400)
        if not User.objects.filter(pk=pk).exists():
            return Response({"detail": "Not found."}, status=404)
        Block.objects.get_or_create(blocker=request.user, blocked_id=pk)
        Like.objects.filter(Q(sender=request.user, recipient_id=pk) | Q(sender_id=pk, recipient=request.user)).delete()
        return Response({"blocked": True})

class ReportView(APIView):
    def post(self, request, pk):
        reason = str(request.data.get("reason", "")).strip()
        if pk == request.user.pk or not User.objects.filter(pk=pk).exists():
            return Response({"detail": "Invalid profile."}, status=400)
        if not 10 <= len(reason) <= 300:
            return Response({"detail": "Reason must be 10-300 characters."}, status=400)
        Report.objects.create(reporter=request.user, reported_id=pk, reason=reason)
        return Response({"reported": True}, status=201)
