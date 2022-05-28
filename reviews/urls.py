from django.urls import path

from reviews.views import list_reviews, create_review, review_detail

urlpatterns = [
    path("", list_reviews, name="reviews_list"),
    path("new/", create_review, name="create_review"),
    path("<int:id>/", review_detail, name="review_detail"),
]