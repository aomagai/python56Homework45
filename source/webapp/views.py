from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import ToDo, STATUS_CHOICES
from django.http import HttpResponseNotAllowed
from .forms import TodoForms


def index_view(request):
    data = ToDo.objects.all()
    return render(request, 'index.html', context={
        'ToDo_list': data
    })

def create_view(request):
    if request.method == "GET":
        form=TodoForms()
        return render(request, 'todo_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = TodoForms(data=request.POST)
        if form.is_valid():
            todo = ToDo.objects.create(
                description=form.cleaned_data['description'],
                detailed_description = form.cleaned_data['detailed_description'],
                status = form.cleaned_data['status'],
                date = form.cleaned_data['date']
            )

            return redirect('todo_view', pk=todo.pk)
        else:
            return render(request, 'todo_create.html', context={
                'form': form
            })
    else:
        HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def delete_item(request, pk):
    ToDo.objects.get(pk=pk).delete()
    return redirect('/')


def todo_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    context = {'todo': todo}
    return render(request, 'todo_view.html', context)

def todo_update_view(request, pk):

    todo = get_object_or_404(ToDo, pk=pk)

    if request.method == "GET":
        return render(request, 'todo_update.html', context={
            'status_choices': STATUS_CHOICES,
            'todo': todo
        })
    elif request.method == 'POST':
        todo.status = request.POST.get('status')
        todo.detailed_description = request.POST.get('detailed_description')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('todo_view', pk=todo.pk)
    else:
        HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

