from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [
    path('hello/', views.show_hello),
    path('cv/', views.my_cv),
    path('add/', views.add),
    path('comment/', views.comment),
    path('session/', views.test_session),

    path('all/',views.MusicList.as_view()),
    path('music/<int:music_id>/',views.MusicView.as_view()),
    # path('music/',views.Music.as_view()),

]