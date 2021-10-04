from django.urls    import path

from comments.views import (
    CommentsGetView,
    CommentsPostView,
)
urlpatterns = [
    path('post',            CommentsPostView.as_view()),
    path('get/<int:id>',    CommentsGetView.as_view()), #id는 post의 id 기준으로 잡아야 함
    path('delete/<int:id>', CommentsGetView.as_view()),
]
