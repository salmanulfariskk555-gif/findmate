from django.urls import path
from .views import MyProfileView, DiscoverView, LikeView, MatchesView, MessageListCreateView, ReportCreateView, BlockView
urlpatterns = [
 path('profile/me/',MyProfileView.as_view(),name='my-profile'),
 path('discover/',DiscoverView.as_view(),name='discover'),
 path('like/<int:user_id>/',LikeView.as_view(),name='like'),
 path('matches/',MatchesView.as_view(),name='matches'),
 path('matches/<int:match_id>/messages/',MessageListCreateView.as_view(),name='messages'),
 path('reports/',ReportCreateView.as_view(),name='report'),
 path('block/<int:user_id>/',BlockView.as_view(),name='block'),
]
