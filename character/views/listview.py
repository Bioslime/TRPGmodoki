from django.db import models
from django.urls.base import reverse
from django.views.generic import ListView, TemplateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from ..models import MonsterModels, SkillModels, YushaModels, RaceModels


class ListTopView(TemplateView):
    template_name = "character/listtop.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "listurl":{"monster":"モンスター", "skill":"スキル","race":"種族","yusha":"勇者"}
        })
        return context


class MonsterListView(ListView):
    model = MonsterModels
    template_name = "character/listdir/monster.html"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        datas = [{"スキル１" : data.skill1} for data in self.model.objects.all()]
        print(datas)
        context.update({
            "sitetag":"モンスター",
            "redirect_url":"character:monsterform",
            "change_url" :"character:monsterupdate",
        })
        return context


class SkillListView(ListView):
    model = SkillModels
    template_name = "character/listdir/skill.html"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "sitetag":"スキル",
            "redirect_url":"character:skillform",
            "change_url" :"character:skillupdate",
        })
        return context


class RaceListView(ListView):
    model = RaceModels
    template_name = "character/listdir/race.html"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "sitetag":"種族",
            "redirect_url":"character:raceform",
            "change_url" :"character:raceupdate",
        })
        return context


class YushaListView(ListView):
    model = YushaModels
    template_name = "character/listdir/yusha.html"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "sitetag":"勇者",
            "redirect_url":"character:yushaform",
            "change_url" :"character:yushaupdate",
        })
        return context

