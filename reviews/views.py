from django.shortcuts import render

from reviews.models import Review


def list_reviews(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/main.html", context)