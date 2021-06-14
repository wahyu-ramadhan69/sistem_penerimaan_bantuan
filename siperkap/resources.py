from import_export import resources
from .models import koperasi, kub, kub_awal


class kubsumber(resources.ModelResource):
    class Meta:
        model = kub_awal


class kubaw(resources.ModelResource):
    class Meta:
        model = kub


class kopsum(resources.ModelResource):
    class Meta:
        model = koperasi
