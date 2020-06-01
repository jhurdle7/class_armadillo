from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='contacts'),
    path('<int:card_id>/', views.detail, name='detail'),
    path('new/', views.entry_page, name='entry_page'),
    path('submit/', views.submit_contact, name='submit_contact'),
]