from django.shortcuts import render

def home(request):
    return render(request, 'rainesProfile/home.html')
