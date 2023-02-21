from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("settings/", views.settings, name="settings"),
    path("search/", views.search, name="search"),
    path("profile/<str:pk>/", views.profile, name="profile"),
    path("upload/", views.upload, name="upload"),
    path("follow/", views.follow, name="follow"),
    path("like-post/", views.like_post, name="like-post"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout, name="logout"),
]
