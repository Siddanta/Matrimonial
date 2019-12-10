from django.shortcuts import render
from .forms import enquiries

def index(request):
    return render(request,'home/index.html')

def aboutus(request):

    return render(request, 'home/aboutus.html')

def enquiry(request):
    if request.method == 'POST':
        form = enquiries(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = enquiries()
    return render(request, 'home/enquiry.html', {'form':form})
