from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    CatalogListView,
    CatalogDetailView,
    ContactTemplateView,
    CatalogCreateView,
    CatalogUpdateView,
    CatalogDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogListView.as_view(), name="product"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("view/<int:pk>/", cache_page(60)(CatalogDetailView.as_view()), name="view"),
    path("create/", CatalogCreateView.as_view(), name="create"),
    path("edit/<int:pk>", CatalogUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>", CatalogDeleteView.as_view(), name="delete"),
]
