from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.utils import timezone
from .models import add_rev

def reviews(request):
    reviews = add_rev.objects.all().order_by('-pub_date')
    return render(request, 'review/view.html', {'review':reviews})

@login_required
def addreview(request):
    if request.method == 'POST':
        if request.POST['body'] and request.POST['score']:
            review = add_rev()
            review.name = request.user
            review.body = request.POST['body']
            review.pub_date = timezone.datetime.now()
            review.img = request.FILES['image']
            review.score = request.POST['score']
            review.save()
            return redirect('reviews')
        else:   
            return render(request,'review/addreview.html', {'error':'All Fields Are Required'})
    else:
        return render(request, 'review/addreview.html')

