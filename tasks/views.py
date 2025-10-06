from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Task


def home(request):
    """
    Show the homepage with the list of all tasks.
    """
    tasks = Task.objects.all().order_by("-id")
    return render(request, "home.html", {"tasks": tasks})


def add_task(request):
    """
    Handle adding a new task via POST (HTMX).
    Returns the updated task list partial.
    """
    if request.method == "POST":
        title = request.POST.get("title")
        if not title:
            return HttpResponseBadRequest("Task title is required.")
        Task.objects.create(title=title)
        tasks = Task.objects.all().order_by("-id")
        return render(request, "partials/task_list.html", {"tasks": tasks})

    # fallback if someone hits add-task without POST
    tasks = Task.objects.all().order_by("-id")
    return render(request, "partials/task_list.html", {"tasks": tasks})


def mark_done(request, task_id):
    """
    Mark a task as done by ID.
    Returns the updated task list partial.
    """
    task = get_object_or_404(Task, id=task_id)
    task.done = True
    task.save()
    tasks = Task.objects.all().order_by("-id")
    return render(request, "partials/task_list.html", {"tasks": tasks})