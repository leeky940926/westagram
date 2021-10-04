from django.urls      import path

from followings.views import FollowingView

urlpatterns = [
    path('post', FollowingView.as_view())
]
