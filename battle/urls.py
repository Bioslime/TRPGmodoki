from django.urls import path
from . import views

app_name = "battle"
urlpatterns =[
    path('index/', views.BattleView.as_view(), name="battle"),
]