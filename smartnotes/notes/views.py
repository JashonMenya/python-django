from django.shortcuts import render

from .models import Notes


def list(request):
    all_notes = Notes.objects.all()
    return render(request, "notes/notes.html", {"notes": all_notes})
