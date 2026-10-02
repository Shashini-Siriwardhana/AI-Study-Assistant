from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Note
from .serializers import NoteSerializer

@api_view(["GET", "POST"])
def notes_list(request):

    if request.method == "GET":
        notes = Note.objects.all()

        serializer = NoteSerializer(
            notes,
            many=True
        )

        return Response(serializer.data)

    if request.method == "POST":
        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "GET":
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = NoteSerializer(
            note,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if request.method == "PATCH":
        serializer = NoteSerializer(
            note,
            data=request.data,
            partial=True
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if request.method == "DELETE":
        note.delete()

        return Response(
            {"message": "Note deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
