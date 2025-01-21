from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import (PostViewSet,
                    CommentViewSet,
                    FollowViewSet)

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register(r"posts/(?P<post_id>\d+)/comments",
                CommentViewSet, basename="comments")
router.register("follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls.jwt")),
]
