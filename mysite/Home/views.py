from django.shortcuts import render

def home(request):
    nama = 'ridho'
    return render(request, 'index.html', {'nama': nama})

def blog(request):
    return render(request, 'blog.html')