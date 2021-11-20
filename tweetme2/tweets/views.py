from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hey</h1>")


def tweet_detail_view(request, tweet_id):
    return HttpResponse(f"<h1>Hello {tweet_id}</h1>")
