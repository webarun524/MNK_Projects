from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# View all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Add a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

# Delete a task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

# Mark task as complete
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Fetch the task or return a 404 if not found
    task.completed = True
    task.save()  # Save the updated task status
    return redirect('task_list')