from re import template
from django.shortcuts import render

from django.views.generic import TemplateView
from .models import MonsterModels, YushaModels


class BattleView(TemplateView):
    template_name = 'battle/battle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mons = MonsterModels.objects.all()
        print(mons)
        context.update({
            'monster_list': mons,
            'yushas': YushaModels,
        })
        return context
