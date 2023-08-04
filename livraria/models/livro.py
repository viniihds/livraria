from django.db import models

from livraria.models import Autor, Categoria, Editora
from uploader.models import Image


class Livro(models.Model):
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )
    autores = models.ManyToManyField(Autor, related_name="livros")

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"
