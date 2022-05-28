from django.shortcuts import render, redirect

from reviews.models import Review
from reviews.forms import ReviewForm

def list_reviews(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/main.html", context)


def create_review(request):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reviews_list")
    context = {
        "form": form,
    }
    return render(request, "reviews/create.html", context)

def review_detail(request, id):
    review = Review.objects.get(id=id)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)