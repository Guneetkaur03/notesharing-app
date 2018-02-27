from django.shortcuts import render
from notes.models import details_notes

# Create your views here.

def notes_list(request):
    notes = details_notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes':notes})
