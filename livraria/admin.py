from django.contrib import admin

from .models import Categoria, Editora, Livro, Autor

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Autor)