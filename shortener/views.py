from django.shortcuts import render, redirect, HttpResponse
from .models import Url
import time
import random
from django.http import Http404

def generate_short_url():
    timestamp_part = str(int(time.time() * 1000))  
    random_part = str(random.randint(1000, 9999))  
    return timestamp_part + random_part

def main_view(request):
    if request.method == "POST":
        result = Url(
            long = request.POST.get('url'),
            short = generate_short_url(),
            short_viewed = 0
        )
        result.save()
        return render(request, 'index.html')
        

    return render(request, 'index.html')

def url_view(request, url):
    urls = Url.objects.get(long=url)
    return redirect('short', short=urls.short)

def short_view(request, short):
    urls = Url.objects.get(short__iexact=short)
    urls.short_viewed += 1
    urls.save()

    return render(request, 'shorter.html', {'urls': urls})


def short_stats(request, short):
    url = Url.objects.get(short=short)
    return render(request, 'stats.html', {'stats': url})