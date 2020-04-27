from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient
from recipe import serializers


class BaseRecipeAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """base viewset for user owner recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """return objects for auth user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serailizer):
        """Create a new attra"""
        serailizer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    """mangane tags in the db"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeAttrViewSet):
    """manage ingreidents in the db"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
