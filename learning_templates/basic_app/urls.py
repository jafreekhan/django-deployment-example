from django.urls import path, include
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    # path('other/', views.other, name='other'),
    # path('relative/', views.relative, name='relative'),
]
