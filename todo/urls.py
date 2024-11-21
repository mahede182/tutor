from django.urls import path
from todo import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('todo/', views.TodoList.as_view()),
    path('todo/<int:pk>', views.TodoDetails.as_view())
    
]

urlpatterns = format_suffix_patterns(urlpatterns)