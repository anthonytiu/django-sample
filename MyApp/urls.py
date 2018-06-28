from django.urls import path
from MyApp.views import MyView

app_name = 'MyApp'

urlpatterns = [
    path('', MyView.as_view()),
]