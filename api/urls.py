from django.urls import path
from api import views

urlpatterns = [
    path('test', views.Test.as_view()),
    path('upload-forms', views.Forms.as_view())
]
