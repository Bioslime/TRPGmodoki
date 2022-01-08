from django.urls import path
from .views import formview, listview, updateview

app_name = "character"
urlpatterns =[
    path("form/monster/", formview.MonsterFormView.as_view(), name="monsterform"),
    path("form/skill/", formview.SkillFormView.as_view(), name="skillform"),
    path("form/race/", formview.RaceFormView.as_view(), name="raceform"),
    path("form/yusha/", formview.YushaFormView.as_view(), name="yushaform"),
    path("form/", formview.FormTopView.as_view(), name="form"),

    path("datalist/monster", listview.MonsterListView.as_view(), name="monsterlist"),
    path("datalist/skill", listview.SkillListView.as_view(), name="skilllist"),
    path("datalist/race", listview.RaceListView.as_view(), name="racelist"),
    path("datalist/yusha", listview.YushaListView.as_view(), name="yushalist"),
    path("datalist/", listview.ListTopView.as_view(), name="listtop"),

    path("form/update/monster/<uuid:pk>/", updateview.MonsterUpdateView.as_view(), name="monsterupdate"),
    path("form/update/skill/<uuid:pk>/", updateview.SkillUpdateView.as_view(), name="skillupdate"),
    path("form/update/race/<uuid:pk>/", updateview.RaceUpdateView.as_view(), name="raceupdate"),
    path("form/update/yusha/<uuid:pk>/", updateview.YushaUpdateView.as_view(), name="yushaupdate"),
]