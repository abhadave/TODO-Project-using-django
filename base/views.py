from django.shortcuts import render,redirect
from base.models import TaskModel,HistoryModel,CompleteModel,RestoreModel
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def home(request):
    news = "📢 Add the new task and perform the crud operation according to your need . Ever ready to get the new task!"
    if 'q' in request.GET:
        q=request.GET['q']
        print(q)
        all_data = TaskModel.objects.filter(Q(title__icontains=q) | Q(desc__icontains=q))
        if len(all_data) == 0:
            return render(request,'home.html',{'nomatch':True})
    else:
        all_data=TaskModel.objects.filter(host=request.user)

    return render(request,'home.html',{'all_data':all_data,'news': news})

def add(request):

    if request.method=='POST':
        title_data=request.POST['title']
        desc_data=request.POST['desc']
        
        TaskModel.objects.create(title=title_data,desc=desc_data,host=request.user)
        return redirect('home')

    return render(request,'add.html')

def details(request, all_tasks):
    for i in TaskModel.objects.all():
        if i.title == all_tasks:
            context = {'all_task': i}
    return render(request,'news_details.html', context )

def about(request):
    return render(request,'about.html')

def edit(request,pk):
    task=TaskModel.objects.get(id=pk)
    print(task.title)

    if request.method == 'POST':
        title_data=request.POST['title']
        desc_data=request.POST['desc']

        task.title = title_data
        task.desc =desc_data
        task.save()
        return redirect('home')

    return render(request,'edit.html',{'task':task})

def delete_(request,pk):
    task=TaskModel.objects.get(id=pk)
    HistoryModel.objects.create(title=task.title,desc=task.desc)
    task.delete()
    return redirect('home')


def confirm_delete(request,pk):
    task=TaskModel.objects.get(id=pk)
   
    return render(request,'confirm_delete.html',{'task':task})


def history(request):

    history_all=HistoryModel.objects.all()
    if len(history_all)==0:
        return render(request,'history.html',{'history_all':history_all,'nohistory':True})

    return render(request,'history.html',{'history_all':history_all})

def delete_history_confirm(request,pk):

        history_task=HistoryModel.objects.get(id=pk)
      
        return render(request,'delete_history_confirm.html',{'history_task':history_task})



def history_delete(request,pk):
    history_task=HistoryModel.objects.get(id=pk)
    history_task.delete()
    return redirect('history')

    
def history_restore(request,pk):
    history_task=HistoryModel.objects.get(id=pk)
    TaskModel.objects.create(title=history_task.title,desc=history_task.desc,host=request.user)
    history_task.delete()
    return redirect('home')


def history_clear(request):
    history_clear_all=HistoryModel.objects.all()
    history_clear_all.delete()
    return redirect('history')


def history_restore_all(request):
    history_all=HistoryModel.objects.all()
    for i in history_all:
        TaskModel.objects.create(title=i.title,desc=i.desc,host=request.user)
    history_all.delete()
    return redirect('history')


def complete_task(request,pk):
    task = TaskModel.objects.get(id=pk)
    CompleteModel.objects.create(title=task.title,desc=task.desc)
    
    task.delete()
    return redirect('completed')


def completed(request):
    tasks = CompleteModel.objects.all()
    
    return render(request,'completed.html',{'task':tasks})