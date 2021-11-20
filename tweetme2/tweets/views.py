from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tweet


def home_view(request, *args, **kwargs):
    print(args, kwargs)

    return render(request, "pages/home.html", context={}, status=200)


def tweet_detail_view(request, tweet_id):
    data = {
        "id": tweet_id,

    }
    try:
        tweet_obj = Tweet.objects.get(id=tweet_id)
        data['content'] = tweet_obj.content
        status = 200
    except:
        data['message'] = "Tweet Not Found"
        status = 404

    # return HttpResponse(f"<h1>Hello {tweet_id} - {tweet_obj.content}</h1>")
    return JsonResponse(data, status=status)
