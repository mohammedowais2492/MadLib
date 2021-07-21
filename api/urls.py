from django.urls import path

from api.views import MadLib

urlpatterns = [
    path('madlib', MadLib.as_view()),
]
