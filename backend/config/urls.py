from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from members.views import RegisterView, MyProfileView, DiscoverView, LikeView, MatchesView, BlockView, ReportView
urlpatterns = [
 path("admin/",admin.site.urls),
 path("api/auth/login/",obtain_auth_token),
 path("api/auth/register/",RegisterView.as_view()),
 path("api/me/",MyProfileView.as_view()),
 path("api/discover/",DiscoverView.as_view()),
 path("api/like/<int:pk>/",LikeView.as_view()),
 path("api/matches/",MatchesView.as_view()),
 path("api/block/<int:pk>/",BlockView.as_view()),
 path("api/report/<int:pk>/",ReportView.as_view()),
]
