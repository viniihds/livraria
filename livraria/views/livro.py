# from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from livraria.models import Livro
from livraria.serializers import (
    CategoriaSerializer,
    EditoraSerializer,
    AutorSerializer,
    LivroSerializer,
    LivroDetailSerializer,
)


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer
