from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /learning_logs/5
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /learning_logs/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /learning_logs/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]