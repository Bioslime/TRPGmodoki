from django.views.generic import UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from ..models import MonsterModels, RaceModels, SkillModels, YushaModels


class MonsterUpdateView(UpdateView):
    template_name = "character/update.html"
    model = MonsterModels
    fields = ("HP", "MP", "skill1","picture")

    def get_success_url(self):
        return reverse_lazy("character:monsterlist")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.get_object().name
        context.update({
            "title":"モンスター情報の変更",
            "name": name,
            "redirect_url" : "character:monsterlist",
        })
        return context

    def get_form(self):
        form = super(MonsterUpdateView,self).get_form()
        form.fields['skill1'].label = 'スキル'
        form.fields['picture'].label = 'モンスターイメージ'
        return form

    def form_valid(self, form):
        form.save()
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "モンスターデータを変更しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "モンスターデータの変更に失敗しました")
        return super().form_invalid(form)


class SkillUpdateView(UpdateView):
    template_name = "character/update.html"
    model = SkillModels
    fields = ("skill_name", "skill_attack",)

    def get_success_url(self):
        return reverse_lazy("character:skilllist")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.get_object().skill_name
        context.update({
            "title":"スキル情報の変更",
            "name": name,
            "redirect_url" : "character:skilllist",
        })
        return context

    def get_form(self):
        form = super(SkillUpdateView, self).get_form()
        form.fields['skill_name'].label = 'スキル名'
        form.fields['skill_attack'].label = '攻撃力'
        return form

    def form_valid(self, form):
        form.save()
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "スキルデータを変更しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "スキルデータの変更に失敗しました")
        return super().form_invalid(form)


class RaceUpdateView(UpdateView):
    template_name = "character/update.html"
    model = RaceModels
    fields = ("race_name", "race_skill",)

    def get_success_url(self):
        return reverse_lazy("character:racelist")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.get_object().race_name
        context.update({
            "title":"種族情報の変更",
            "name": name,
            "redirect_url" : "character:racelist",
        })
        return context

    def get_form(self):
        form = super(RaceUpdateView, self).get_form()
        form.fields['race_name'].label = '種族名'
        form.fields['race_skill'].label = '種族スキル'
        return form

    def form_valid(self, form):
        form.save()
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "種族データを変更しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "種族データの変更に失敗しました")
        return super().form_invalid(form)


class YushaUpdateView(UpdateView):
    template_name = "character/update.html"
    model = YushaModels
    fields = ("HP", "MP", "lv", "race", "skill1","picture")

    def get_success_url(self):
        return reverse_lazy("character:yushalist")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.get_object().name
        context.update({
            "title":"勇者情報の変更",
            "name": name,
            "redirect_url" : "character:yushalist",
        })
        return context

    def get_form(self):
        form = super(YushaUpdateView, self).get_form()
        form.fields['skill1'].label = 'スキル'
        form.fields['lv'].label = 'レベル'
        form.fields['race'].label = '種族'
        form.fields['picture'].label = 'キャラクターイメージ'
        return form

    def form_valid(self, form):
        form.save()
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "勇者データを変更しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "勇者データの変更に失敗しました")
        return super().form_invalid(form)