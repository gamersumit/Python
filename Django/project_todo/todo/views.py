from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task

# Create your views here.
def index(request):
    return render(request, 'index.html') # render index.html

#<!---------add function to add new tasks ----------->
def add(request):
    if request.method == 'POST':       # after proving inputs
        title = request.POST.get('title') # get those inputs
        body = request.POST.get('body') 
           
        if (not title) or (not body ):   # check if inputs are not empty
            messages.info(request, 'All fileds are required')
            return redirect('add')
        
        elif Task.objects.filter(title=title).exists() :   # if a task with same title already present
            messages.info(request, 'Task already exists')
            return redirect('add')
        
        else:                                                   # else add a new task to database
            task = Task.objects.create(title=title, body=body)
            task.save()
            return redirect('index')

    else :              # if inputs are not provided yet render add.html to create a interface to get those inputs
        return render(request, 'add.html')
    
# <!----------- end add -------- >


# <! ---------- view to display all tasks ------->    
def view(request):
    tasks = Task.objects.all()   # get all objects of task from database
    return render(request, 'view.html', {'tasks': tasks})

# <! ---------- end view -------- >


#<!------------ delete to task objects ------>

def delete(request):
    if request.method == 'POST':  # after taking inputs
        title = request.POST['title']

        if not title:   # check if title is empty or not
            messages.info(request, 'Empty title field')
            return redirect('delete')
        
        elif Task.objects.filter(title=title).exists() :   # if title found delete it
            task = Task.objects.get(title=title)
            task.delete()
            return redirect('index')
            
        else:                       # if title not found
            messages.info(request, 'Task not found')
            return redirect('delete')
            
    else :  # before provinding inputs display interface to take inputs
        return render(request, 'delete.html')

#<! ------------- end delete ------------- >
    
#<! ------------- edit to edit details of task --------------- >
def edit(request):
    if request.method == 'POST':  # if inputs are provided
        title = request.POST.get('title') # getting all inputs (title to access that perticular task among all which user want to edit) 
        head = request.POST.get('head') == 'on' # fields/properties that user want to edit if 'on' means user want to edit that perticular filled
        body = request.POST.get('body') == 'on'
        status = request.POST.get('status') == 'on'

        if not title: # if title provided is empty
            messages.info(request, 'Title cannot be empty')
            return redirect('edit')
        
        elif not head and not body and not status :  # if all the properties of task are not selected to edit
            messages.info(request, 'You have to choose atleast one option to edit')
            return redirect('edit')
           
        elif Task.objects.filter(title=title).exists() :  # if task found with the provided title go to next step to edit details
            task_id = Task.objects.get(title=title).id
            return render(request, 'edit_details.html', {'task':task_id,'status':status,'title':head,'body': body})
       
        else: # if task not found with the provided title
            messages.info(request, 'Task not found')
            return redirect('edit')

    else : # if inputs are not provided yet show interface to get inputs
        return render(request, 'edit.html')

# <!------------ end edit ------------>
    

# <! --------- edit details to edit after verifying all the condition in edit view function -- >
def edit_details(request): 

    status = request.POST.get('status') == 'True'  # getting details sent by edit view 
    title = request.POST.get('title') == 'True'      
    body = request.POST.get('body') == 'True'
    newstatus = request.POST.get('newstatus') == 'on' # getting new details which we want to add to the task at the place of old ones
    newtitle = request.POST.get('newtitle') 
    newbody = request.POST.get('newbody') 
    task = request.POST.get('task')

    if title : # checking if title was selected to edit
        if not newtitle : # if new title is empty
            print('newtitle')
            messages.info(request, 'Title should not be empty')
            return render(request, 'edit_details.html', {'task': task,'body': body, 'title': title, 'status': status})

        elif Task.objects.filter(title=newtitle).exists() : # new title is matched with an task with same title
            print('exists')
            messages.info(request, 'Task with same title already exists')
            return render(request, 'edit_details.html', {'task': task,'body': body, 'title': title, 'status': status})
    
    if body and (not newbody) : # if body was selected to edit and newbody is empty
        print('here')
        messages.info(request, 'Body should not be empty')
        return render(request, 'edit_details.html', {'task': task,'body': body, 'title': title, 'status': status})
    
    task = Task.objects.get(id=task) # if all conditons are satisfied add new details in place of old ones
    if title: # if title was selected repalce it with newtitle
        task.title = newtitle
    if status: # if stauts was selected replace with newstatus
        task.status = newstatus
    if body: # if body was selected repalace it with newbody
        task.body = newbody

    task.save() # saves edited details and  redirect user to home page/index page
    return redirect('index')
    
    

