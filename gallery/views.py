from django.shortcuts import render

def gallery(request):
    return render(request, 'gall/view_gallery.html')
