from django.contrib import admin
from django.urls import path
from. import views

app_name = 'account'

urlpatterns = [
    path('users/', views.index_account, name="account"),
]
