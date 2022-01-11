from django.views.generic import CreateView, TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from..forms import MonsterRegisterForm, SkillRegisterForm, RaceRegisterForm, YushaRegisterForm

# Create your views here.



class FormTopView(TemplateView):
    template_name = "character/formtop.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "formurl":{"monster":"モンスター", "skill":"スキル","race":"種族","yusha":"勇者"}
        })
        return context


class MonsterFormView(CreateView):
    form_class = MonsterRegisterForm
    template_name = "character/dataform.html"
    success_url = reverse_lazy("character:monsterlist")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title":"モンスター情報の登録",
            "redirect_url":"character:monsterlist",
            "redirect_tag":"モンスター一覧",
        })
        return context

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
    template_name = "character/dataform.html"
    success_url = reverse_lazy("character:skilllist")

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title":"スキル情報の登録",
            "redirect_url":"character:skilllist",
            "redirect_tag":"スキル一覧",
        })
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "新規スキルデータを作成しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "新規スキルデータの作成に失敗しました")
        return super().form_invalid(form)


class RaceFormView(CreateView):
    form_class = RaceRegisterForm
    template_name = "character/dataform.html"
    success_url = reverse_lazy("character:racelist")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title":"種族情報の登録",
            "redirect_url":"character:racelist",
            "redirect_tag":"種族一覧",
        })
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "新規種族データを作成しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "新規種族データの作成に失敗しました")
        return super().form_invalid(form)


class YushaFormView(CreateView):
    form_class = YushaRegisterForm
    template_name = "character/dataform.html"
    success_url = reverse_lazy("character:yushalist")

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title":"勇者情報の登録",
            "redirect_url":"character:yushalist",
            "redirect_tag":"勇者一覧",
        })
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "新規勇者データを作成しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        [m for m in messages.get_messages(self.request)]
        messages.success(self.request, "新規勇者データの作成に失敗しました")
        return super().form_invalid(form)

