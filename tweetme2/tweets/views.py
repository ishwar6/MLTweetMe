from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils.http import is_safe_url


from tweets.forms import TweetForm
from .models import Tweet
import random
from django.conf import settings


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    print(args, kwargs)
   # print(request.sessions)
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    print(request.session)

    return render(request, "pages/home.html", context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content,
                    "likes": random.randint(0, 2322)} for x in qs]
    data = {
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_create_form(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    print(request.POST)
    next_url = request.POST.get("next") or None
    print(next_url)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url is not None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'tweets/forms.html', context={"form": form})


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
