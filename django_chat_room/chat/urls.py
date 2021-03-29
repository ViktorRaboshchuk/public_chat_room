
from django.urls import path, include

from chat import views

urlpatterns = [
    path('list/', views.MessageListView.as_view()),
    path('single/<int:pk>/', views.MessageDetailView.as_view()),
    path('send/', views.MessageCreateView.as_view()),
    path('update/<int:pk>/', views.MessageUpdateView.as_view()),
]
