from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_blog, name='create-my_blogger'),
    path('search/', views.retrieve_blog, name='retrieve-my_blogger'),
    path('update/<int:pk>', views.update_blog, name='update-my_blogger'),
    path('delete/<int:pk>', views.delete_blog, name='delete-my_blogger'),
]
