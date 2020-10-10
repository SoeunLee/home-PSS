from django.urls import path # to resolve NameError: Name 'path' is not defined
from blog import views # to resolve NameError: name 'views' is not defined

urlpatterns = [
    path('', views.post_list, name='post_list'),
]