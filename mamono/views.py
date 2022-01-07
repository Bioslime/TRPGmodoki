from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import MonsterModels
from.forms import MonsterRegisterForm, SkillRegisterForm

# Create your views here.

class MonsterFormView(CreateView):
    form_class = MonsterRegisterForm
    template_name = "mamono/monsterform.html"
    success_url = reverse_lazy("mamono:mosterform")

    def form_valid(self, form):
        form.instance.user = self.request.user
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "新規モンスターデータを作成しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "新規モンスターデータの作成に失敗しました")
        return super().form_invalid(form)


class SkillFormView(CreateView):
    form_class = SkillRegisterForm
    template_name = "mamono/skillform.html"
    success_url = reverse_lazy("mamono:skillform")

    def form_valid(self, form):
        form.instance.user = self.request.user
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "新規スキルデータを作成しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "新規スキルデータの作成に失敗しました")
        return super().form_invalid(form)
