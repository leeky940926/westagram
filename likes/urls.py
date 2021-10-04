from django.urls import path

from likes.views import LikeView

urlpatterns = [
    path('post', LikeView.as_view())
]
