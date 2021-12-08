

from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', include('data.urls')),
]

l = ['a', 'b', 'c', bca]


def repeated(l):
    if len(l) > 0:
        s = set()
        for i in l:
            if i in s:
                return i
            else:
                s.add(i)
