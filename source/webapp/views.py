from django.shortcuts import render
from webapp.models import ToDo, STATUS_CHOICES


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
        description = request.POST.get('description')
        print(description)
        todo = ToDo.objects.create( description=description, status=status, date=date)
        context = {'todo': todo}
        return render(request, 'todo_view.html', context)
