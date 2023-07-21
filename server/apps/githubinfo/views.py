from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from celery.result import AsyncResult
from .tasks import request_githubinfo
from server.celery import app


def create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        task = request_githubinfo.delay(request.POST['username'])
        return render(request, 'githubinfo/detail.html', context={"id": task.id})
    else:
        return render(request, 'githubinfo/create.html')


def detail(request: HttpRequest) -> HttpResponse:
    id = request.GET['id']
    task = AsyncResult(id, app=app)
    return render(request, 'githubinfo/detail.html',
                  context={"id": id, "status": task.status, "state": task.state, "result": task.result,
                           "is_error": isinstance(task.result, str)})
