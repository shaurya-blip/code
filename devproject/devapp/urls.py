from django.urls import path
from .views import IndexClass,IndexDetail,CommentList,add_comment_to_post

urlpatterns = [
    path('comment/new/in/post/<int:pk>/',add_comment_to_post,name='comment_new'),
    path('comment/in/post/<int:pk>/',CommentList.as_view(),name="comment-list"),
    path('',IndexClass.as_view(),name='home'),
    path('post/<int:pk>/',IndexDetail.as_view(),name='post-detail'),
]