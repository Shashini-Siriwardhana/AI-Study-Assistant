from rest_framework import serializers
from .models import Note

# Convert Django object to Json
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"