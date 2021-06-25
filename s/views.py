from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UsedUrlData
from .forms import Url
import sys
import json


def index(request):
    form = Url()
    context = {
        'form': form,
    }
    return render(request, 's/index.html', context)


def urlShort(request):
    if request.method == 'POST':
        # @$ in order to process the curl post request
        body_unicode = request.body.decode('utf-8')
        normalized_string = str(body_unicode)
        address_start = normalized_string.find('http')
        address_end = normalized_string.find('}')
        actual_url = normalized_string[address_start:address_end]+'/'
        new_url_object = UsedUrlData(url=actual_url)
        new_url = new_url_object.get_short_url()
        new_url_object.save()
        return HttpResponse(new_url)
    else:
        return Http404()


def urlRedirect(request, short_url):
    try:
        data = UsedUrlData.objects.get(short_url=short_url)
        return redirect(data.url)
    except:
        return Http404()
