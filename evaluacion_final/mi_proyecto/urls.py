from django.contrib import admin
from django.urls import path, include  # <-- agrega include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("notas/", include("app_notas.urls")),  # <-- agrega esta línea
]
