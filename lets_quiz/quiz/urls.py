from django.urls import re_path,include
from . import views


app_name = 'quiz'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^play/$', views.play, name='play'),
    re_path(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
    re_path(r'^submission-result/(?P<attempted_question_pk>\d+)/', views.submission_result, name='submission_result'),
    re_path(r'^login/', views.login_view, name='login'),
re_path(r'^notsubmission_result/', views.notsubmission_result, name='notsubmission_result'),
    re_path(r'^logout/', views.logout_view, name='logout'),
    re_path(r'^register/', views.register, name='register'),
    re_path(r'^paymentdone/', views.payment_done, name='paymentdone'),

]
