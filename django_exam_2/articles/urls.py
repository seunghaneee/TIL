from django.urls import path
from . import views
app_name='articles'
urlpatterns = [
    # index
    path('', views.index, name='index'),
    # create
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # Read
    path('<int:pk>/', views.detail, name='detail'),
    # Delete
    path('<int:pk>/delete/', views.delete, name='delete'),
    # Update
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update')
]
