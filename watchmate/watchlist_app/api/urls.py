from django.urls import path, include
from watchlist_app.api import views
urlpatterns = [
    path('',views.WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>',views.WatchListDetailAV.as_view(),name='movie-detail'),
    path('stream/',views.StreamPlatformAV.as_view(),name='stream'), 
    path('stream/<int:pk>/',views.StreamDetailAV.as_view(),name='stream-detail')
]
