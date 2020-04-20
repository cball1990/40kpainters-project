from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.utils import timezone
from .models import add_review

def reviews(request):
    reviews = add_review.objects.all()
    return render(request, 'review/view.html', {'review':reviews})

@login_required
def addreview(request):
    if request.method == 'POST':
        if request.POST['body'] and request.POST['url'] and request.FILES['image']:
            review = add_review()
            review.name = request.user
            review.body = request.POST['body']
            review.pub_date = request.POST['pub_date']
            review.image = request.POST['image']
            review.score = request.POST['score']
            review.save()
            return redirect(request, 'review/reviews.html')
        else:   
            return render(request,'review/addreview.html', {'error':'All Fields Are Required'})
    else:
        return render(request, 'review/addreview.html')

