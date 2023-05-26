from django.contrib import admin
from django.urls import include, path

# from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("home.urls", "home"))),
    path("venta/", include(("venta.urls", "venta"))),
    path("producto/", include(("producto.urls", "producto"))),
]

# Ejemplo --> path("producto/", include(("producto.urls", "producto"))),
# 1er parametro - la url
# 2do parametro - include --> que incluya todas las urls dentro de producto.url
# 1er parametro include - archivo del cual s equiere incluir todas sus urls
# 2do parametro include - nombre que se le asignara a ese grupo de urls para luego referenciarlas en las plantillas html
