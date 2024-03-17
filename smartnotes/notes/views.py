from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

from .models import Notes
from .forms import NotesForm


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes   
    success_url = '/smart/notes'
    form_class = NotesForm


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
    success_url = '/smart/notes'
    # fields = ['title', 'text'] --->> replacing with model forms down below
    form_class = NotesForm


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, "notes/notes.html", {"notes": all_notes})


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404(f"Note with primary key:{pk},Does not Exist")

#     return render(request, "notes/notes_details.html", {"note": note})
