from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')

        if (not title) or (not body ):
            messages.info(request, 'All fileds are required')
            return redirect('add')
        
        elif Task.objects.filter(title=title).exists() :
            messages.info(request, 'Task already exists')
            return redirect('add')
        
        else:
            task = Task.objects.create(title=title, body=body)
            task.save()
            return redirect('index')

    else :
        return render(request, 'add.html')
    
def view(request):
    tasks = Task.objects.all()
    return render(request, 'view.html', {'tasks': tasks})

def delete(request):
    if request.method == 'POST':
        title = request.POST['title']

        if not title:
            messages.info(request, 'Empty title field')
            return redirect('delete')
        
        elif Task.objects.filter(title=title).exists() :
            task = Task.objects.get(title=title)
            task.delete()
            return redirect('index')
            
        else:
            messages.info(request, 'Task not found')
            return redirect('delete')
            
    else :
        return render(request, 'delete.html')
    

def edit(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        choice = request.POST.get('choice')
        print(choice, type(choice))
        if (not title) or (not choice):
            messages.info(request, 'All fileds are required')
            return redirect('edit')
        
        elif choice != '0' and choice != '1' and choice != '2':
            messages.info(request, 'Invalid choice')
            return redirect('edit')
        
        elif Task.objects.filter(title=title).exists() :
            task = Task.objects.get(title=title)

            if choice == '0': 
                return redirect('edit/title')
            elif choice == '1':
                return redirect('edit/body')
            else :
                return redirect('edit/status')
        
        else:
            messages.info(request, 'Task not found')
            return redirect('edit')

    else :
        return render(request, 'edit.html')
    
