from django.http import HttpResponse
from django.shortcuts import render


def index_page(request):

    project_name = 'Giocatory Blog'

    return render(request, './index.html', {
        'name': 'Mikhail',
        'project': project_name
    })
