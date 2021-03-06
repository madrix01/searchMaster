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
                'maxResults' : 1,
                'type' : 'video',
            }
            r = requests.get(search_url, params=params)
            res = r.json()['items']
            res_id = []
            res_title = []
            x = range(len(result))
            for i in res:
                res_id.append(i['id']['videoId'])
            print(res_id)
            for i in res:
                res_title.append(i['snippets']['title'])

    else:
        form = SearchForm()
        res = ""
        res_id = []
        res_title = []
        x = 0
    return render(request, "main/search.html", {
        "form":form,
        'res' : res,
        'result': result,
        'x': x,
    })