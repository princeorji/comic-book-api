from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.get_routes, name='get-routes'),

    # auth
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # artists
    path('get-artists/', views.get_artists, name='get-artists'),
    path('artist/<int:pk>/', views.artist, name='artist'),
    path('create-artist/', views.create_artist, name='create-artist'),
    path('update-artist/<int:pk>/', views.update_artist, name='update-artist'),

    # series
    path('get-series/', views.get_series, name='get-series'),
    path('series/<int:pk>/', views.series, name='series'),
    path('create-series/', views.create_series, name='create-series'),
    path('update-series/<int:pk>/', views.update_series, name='update-series'),
    path('delete-series/<int:pk>/', views.delete_series, name='delete-series'),

    # issue
    path('series/<int:pk>/issues/', views.get_issues_by_series, name='issues-by-series'),
    path('issue/<int:pk>/', views.issue, name='issue'),
    path('create-issue/', views.create_issue, name='create-issue'),
    path('update-issue/<int:pk>/', views.update_issue, name='update-issue'),
    path('delete-issue/<int:pk>/', views.delete_issue, name='delete-issue'),
]