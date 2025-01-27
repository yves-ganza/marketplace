from django.urls import path

from . import views

app_name = 'inbox'

urlpatterns = [
    path('', views.inbox, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:item_pk>/', views.new, name='new')
]