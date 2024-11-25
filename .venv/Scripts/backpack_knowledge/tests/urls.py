from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('test/create/<int:topic_id>/', views.test_create, name='test_create'),
    #path('test/<int:test_id>/', views.test_detail, name='test_detail'),  # Маршрут для перегляду тесту    
    path('test/test/<int:test_id>/', views.test_detail, name='test_detail'),
    #path('test/pass/<int:test_id>/', views.test_pass, name='test_pass'),
    path('tests/test/pass/<int:test_id>/', views.pass_test, name='test_pass'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('subjects/topic/<int:topic_id>/results/', views.topic_results, name='topic_results'),

]
