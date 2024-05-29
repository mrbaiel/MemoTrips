# memotrips/trips/urls.py
from django.urls import path
from trips import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/<int:pk>/edit/', views.edit_note, name='edit_note'),
    path('notes/<int:pk>/delete/', views.delete_note, name='delete_note'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
]
