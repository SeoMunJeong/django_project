from django.urls import path
from . import views
from .views import PollsDeleteView

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('result/', views.allResultView.as_view(), name='result'),
    path('delete/<int:pk>/', PollsDeleteView.as_view(), name='delete'),
]