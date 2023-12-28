from django.shortcuts import render

# Create your views here.

def displayFeed(request):
    return render(request, 'feed/feed.html', {})