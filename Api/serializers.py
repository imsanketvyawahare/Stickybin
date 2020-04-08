from rest_framework import serializers
from Application.models import Sticky


class StickyApi(serializers.ModelSerializer):
    class Meta:
        model = Sticky
        fields = ["title", "note", "date", "slug"]

