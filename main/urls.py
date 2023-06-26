from django.urls import path

from main import views


urlpatterns = [
    path('saved/', views.SavedCandidatesView.as_view(), name='saved'),
    path('candidates/', views.CandidatesView.as_view(), name='candidates'),
    path('candidates/<int:pk>/', views.CandidatesDetailView.as_view(), name='candidates_detail'),
]