from django.urls import path


from .views import ListTodo, DetailTodo

urlpatterns = [
    path('<ink:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
]
