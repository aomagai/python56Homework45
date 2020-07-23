from django.shortcuts import render
from webapp.models import ToDo, STATUS_CHOICES


def index_view(request):
    data = ToDo.objects.all()
    return render(request, 'index.html', context={
        'ToDo_list': data
    })
