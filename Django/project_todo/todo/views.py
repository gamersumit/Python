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
        head = request.POST.get('head') == 'on'
        body = request.POST.get('body') == 'on'
        status = request.POST.get('status') == 'on'

        if not title:
            messages.info(request, 'Title cannot be empty')
            return redirect('edit')
        
        elif not head and not body and not status :
            messages.info(request, 'You have to choose atleast one option to edit')
            return redirect('edit')
           
        elif Task.objects.filter(title=title).exists() :
            task_id = Task.objects.get(title=title).id
            return render(request, 'edit_details.html', {'task':task_id,'status':status,'title':head,'body': body})
       
        else:
            messages.info(request, 'Task not found')
            return redirect('edit')

    else :
        return render(request, 'edit.html')
    


def edit_details(request):

    status = request.POST.get('status') == 'True'
    title = request.POST.get('title') == 'True'
    body = request.POST.get('body') == 'True'
    newstatus = request.POST.get('newstatus') == 'on'
    newtitle = request.POST.get('newtitle')
    newbody = request.POST.get('newbody') 
    task = request.POST.get('task')
    print('checking')
    print(body,type(body), 'body')
    print(newbody,type(newbody), 'newbody')

    if title :
        if not newtitle :
            print('newtitle')
            messages.info(request, 'Title should not be empty')
            return render(request, 'edit_details.html', {'task': task,'body': body, 'title': title, 'status': status})

        elif Task.objects.filter(title=newtitle).exists() :
            print('exists')
            messages.info(request, 'Task with same title already exists')
            return render(request, 'edit_details.html', {'task': task,'body': body, 'title': title, 'status': status})
    
    if body and (len(newbody) == 0) :
        print('here')
        messages.info(request, 'Body should not be empty')
        return render(request, 'edit_details.html', {'task': task,'body': body, 'title': title, 'status': status})
    
    task = Task.objects.get(id=task)
    if title: 
        task.title = newtitle
    if status: 
        task.status = newstatus
    if body: 
        task.body = newbody

    task.save()
    return redirect('index')
    
    

