from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api'
urlpatterns = [
    path('skill/', views.SkillListCreateView.as_view(), name='skilllist'),
    path('skill/<uuid:pk>', views.SlkillDetailView.as_view(), name='skilldetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)