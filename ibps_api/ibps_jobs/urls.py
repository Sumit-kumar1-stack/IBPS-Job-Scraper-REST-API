from django.urls import path
from .views import LoginView, JobListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('jobs/', JobListView.as_view(), name='list_jobs'),
]
