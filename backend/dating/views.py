from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile, Like, Match, Conversation, Message, Report, Block
from .serializers import ProfileSerializer, MessageSerializer, ReportSerializer

class MyProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request): return Response(ProfileSerializer(request.user.profile).data)
    def patch(self, request):
        serializer=ProfileSerializer(request.user.profile,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True); serializer.save(); return Response(serializer.data)

class DiscoverView(generics.ListAPIView):
    serializer_class=ProfileSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        blocked=Block.objects.filter(Q(blocker=user)|Q(blocked=user)).values_list('blocker_id','blocked_id')
        excluded={user.id}
        for a,b in blocked: excluded.update([a,b])
        return Profile.objects.filter(is_visible=True).exclude(user_id__in=excluded).exclude(user__received_likes__sender=user)

class LikeView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request,user_id):
        if user_id == request.user.id: raise ValidationError('You cannot like your own profile.')
        if Block.objects.filter(Q(blocker=request.user,blocked_id=user_id)|Q(blocker_id=user_id,blocked=request.user)).exists(): raise PermissionDenied('This action is unavailable.')
        receiver=User.objects.filter(id=user_id,is_active=True).first()
        if not receiver or not hasattr(receiver,'profile') or not receiver.profile.is_visible: raise ValidationError('Profile not available.')
        with transaction.atomic():
            Like.objects.get_or_create(sender=request.user,receiver=receiver)
            mutual=Like.objects.filter(sender=receiver,receiver=request.user).exists()
            if mutual:
                one,two=sorted([request.user,receiver],key=lambda u:u.id)
                match,_=Match.objects.get_or_create(user_one=one,user_two=two)
                Conversation.objects.get_or_create(match=match)
                return Response({'matched':True,'match_id':match.id},status=status.HTTP_201_CREATED)
        return Response({'matched':False},status=status.HTTP_200_OK)

class MatchesView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        qs=Match.objects.filter(Q(user_one=request.user)|Q(user_two=request.user)).select_related('user_one__profile','user_two__profile')
        data=[]
        for m in qs:
            other=m.user_two if m.user_one_id==request.user.id else m.user_one
            data.append({'id':m.id,'created_at':m.created_at,'profile':ProfileSerializer(other.profile).data})
        return Response(data)

class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class=MessageSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        conv=Conversation.objects.filter(match_id=self.kwargs['match_id']).filter(Q(match__user_one=self.request.user)|Q(match__user_two=self.request.user)).first()
        if not conv: raise PermissionDenied('Conversation not available.')
        return conv.messages.select_related('sender').order_by('created_at')
    def perform_create(self,serializer):
        conv=Conversation.objects.filter(match_id=self.kwargs['match_id']).filter(Q(match__user_one=self.request.user)|Q(match__user_two=self.request.user)).first()
        if not conv: raise PermissionDenied('Conversation not available.')
        serializer.save(conversation=conv,sender=self.request.user)

class ReportCreateView(generics.CreateAPIView):
    serializer_class=ReportSerializer
    permission_classes=[permissions.IsAuthenticated]
    def perform_create(self,serializer):
        target=serializer.validated_data['reported_user']
        if target.id==self.request.user.id: raise ValidationError('You cannot report your own account.')
        serializer.save(reporter=self.request.user)

class BlockView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request,user_id):
        if user_id==request.user.id: raise ValidationError('You cannot block yourself.')
        target=User.objects.filter(id=user_id).first()
        if not target: raise ValidationError('User not found.')
        Block.objects.get_or_create(blocker=request.user,blocked=target)
        Like.objects.filter(Q(sender=request.user,receiver=target)|Q(sender=target,receiver=request.user)).delete()
        return Response({'blocked':True})
