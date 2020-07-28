from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import ToDo, STATUS_CHOICES
from django.http import HttpResponseNotAllowed
from django.urls import reverse



def index_view(request):
    data = ToDo.objects.all()
    return render(request, 'index.html', context={
        'ToDo_list': data
    })

def create_view(request):
    if request.method == "GET":
        return render(request, 'todo_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        status = request.POST.get('status')
        date = request.POST.get('date')
        detailed_description = request.POST.get('detailed_description')

        if date == '':
            date = None
        description = request.POST.get('description')
        todo = ToDo.objects.create(description=description, status=status, date=date, detailed_description=detailed_description)
        return redirect('todo_view', pk=todo.pk)
    else:
        HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def delete_item(request, pk):
    ToDo.objects.get(pk=pk).delete()
    return redirect('/')


def todo_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    context = {'todo': todo}
    return render(request, 'todo_view.html', context)
