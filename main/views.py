from django.shortcuts import render
from .models import * 
from .forms import *
from django.conf import settings
import requests



def home(request):
    return render(request, "main/home.html", {})


def TagView(request):
    if request.method == "POST":
        form = AddTags(request.POST)
        if form.is_valid():
            tags = form.cleaned_data["tags"]
            u = Tags(tags=tags)
            u.save()
    else:
        form = AddTags()
    return render(request, "main/tag.html", {
        "form":form,
    })


def SearchView(request):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            tags = form.cleaned_data["tags"]
            u = History(search=search, tags=tags)
            u.save()
            params = {
                'part' : 'snippet',
                'q' : f"{search}+{tags}",
                'key' : settings.YOUTUBE_DATA_API_KEY,
                'maxResults' : 9,
                'type' : 'video',
            }
            r = requests.get(search_url, params=params)
            res = r.json()['items']
            result = []
            x = range(len(result))
            for i in res:
                result.append(i['id']['videoId'])
            print(result)

    else:
        form = SearchForm()
        res = ""
        result = []
        x = 0
    return render(request, "main/search.html", {
        "form":form,
        'res' : res,
        'result': result,
        'x': x,

    })