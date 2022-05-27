from django.urls import path

from reviews.views import list_reviews

urlpatterns = [
    path("", list_reviews, name="reviews_list"),
]