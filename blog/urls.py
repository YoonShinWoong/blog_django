from django.urls import path
from . import views

urlpatterns=[
    path('<int:blog_id>', views.detail, name="detail"),
    path('new/', views.new,name="new"),
    path('create/', views.create, name='create'),
    path('newblog', views.blogpost, name="newblog"),
    path('newreply',views.newreply, name="newreply"),
    path('<int:blog_id>/editBlog/', views.blogedit, name="blogedit"),
]