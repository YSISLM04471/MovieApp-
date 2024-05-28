from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'movies': ['interstellar', 'The holiday', 'Alien Movie', 'Rambo IV']
    }
    return render(request, 'movies/index.html',context)

def about(request):
    return render(request, 'movies/about.html', {})    
