from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView

from .models import Notes


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    # optional
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"


class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = '/smart/notes'
    
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, "notes/notes.html", {"notes": all_notes})


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404(f"Note with primary key:{pk},Does not Exist")

#     return render(request, "notes/notes_details.html", {"note": note})
