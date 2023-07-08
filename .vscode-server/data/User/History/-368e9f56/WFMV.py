from django.shortcuts import render

def Home(request):
    return render(request, 'netflixpp/index.html')
# Create your views here.
