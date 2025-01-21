
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueValidator

from posts.models import Comment, Post, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username",
                              read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field="username")

    class Meta:
        fields = "__all__"
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username",
        default=serializers.
        CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
    )
    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=["user", "following"]
        )
    ]

    def validate(self, data):
        if (self.context["request"].
                user != data["author"]):
            return data
        raise (serializers.
               ValidationError("На тебя нельзя подписаться"))

    class Meta:
        fields = "__all__"
        model = Follow
