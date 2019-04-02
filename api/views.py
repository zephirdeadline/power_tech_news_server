from django.http import HttpResponse
from django.shortcuts import render

# Create your views_api here.
from rest_framework.decorators import api_view

from api.models import Rss
from api.tools.initdata import initdata


def init(request):
    initdata()
    return HttpResponse('ok')


@api_view(['GET'])
def set_as_read(request, id_rss):
    Rss.objects.get(id=id_rss).user_read.add(request.user)
    return HttpResponse('ok')
