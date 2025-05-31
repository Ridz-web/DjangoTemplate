from django.shortcuts import render

def home(request):
    nama = 'ridho'
    return render(request, 'Home/index.html', {'nama': nama})

def blog(request):
    return render(request, 'Home/blog.html')