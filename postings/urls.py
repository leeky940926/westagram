from django.urls    import path

from postings.views import PostingView, PostingUpdateView

urlpatterns = [
    path('post',           PostingView.as_view()),
    path('delete/<int:id>',PostingView.as_view()),
    path('post/<int:id>'  ,PostingUpdateView.as_view())
]
