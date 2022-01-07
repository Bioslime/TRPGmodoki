from django.urls import path
from . import views

app_name = "mamono"
urlpatterns =[
    path("monster_form/", views.MonsterFormView.as_view(), name="mosterform"),
    path("skill_form/", views.SkillFormView.as_view(), name="skillform"),
]