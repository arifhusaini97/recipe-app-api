from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from recipe import serializers


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage tags in the database"""

    # The variables here are all reserved. So make sure the name is correct.
    # 'TagViewSet' should either include a `serializer_class` attribute,
    # or override the `get_serializer_class()` method.
    
    authentication_classes = {TokenAuthentication, }
    permission_classes = {IsAuthenticated, }
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""

        return self.queryset.filter(user=self.request.user).order_by('-name')
