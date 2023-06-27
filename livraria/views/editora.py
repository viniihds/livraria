from rest_framework.viewsets import ModelViewSet
from livraria.models import Editora

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer