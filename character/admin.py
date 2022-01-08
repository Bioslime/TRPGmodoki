from django.contrib import admin
from .models import MonsterModels, SkillModels, RaceModels, YushaModels

admin.site.register(MonsterModels)
admin.site.register(SkillModels)
admin.site.register(RaceModels)
admin.site.register(YushaModels)

# Register your models here.
