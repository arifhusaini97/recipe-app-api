from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from recipe import serializers

class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage tags in the database"""
    authentication_classes ={TokenAuthentication,}
    permissions_classes ={IsAuthenticated,}
    queryset = Tag.objects.all()
    serializers_class = serializers.TagSerializer
