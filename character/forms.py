from django import forms
from .models import MonsterModels, SkillModels, YushaModels, RaceModels


class MonsterRegisterForm(forms.ModelForm):
    class Meta:
        model = MonsterModels
        fields = ("name", "HP", "MP", "skill1", "picture",)
        labels = {
            "name":"モンスター名",
            "skill1":"スキル1",
            "picture":"モンスターイメージ",
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class SkillRegisterForm(forms.ModelForm):
    class Meta:
        model = SkillModels
        fields = ("skill_name","skill_attack",)
        labels={
            "skill_name":"スキル名称",
            "skill_attack":"攻撃力",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class RaceRegisterForm(forms.ModelForm):
    class Meta:
        model = RaceModels
        fields = ("race_name", "race_skill",)
        labels = {
            "race_name":"種族名",
            "race_skill":"種族スキル",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class YushaRegisterForm(forms.ModelForm):
    class Meta:
        model = YushaModels
        fields = ("name", "race", "lv", "HP", "MP", "skill1", "picture",)
        labels = {
            "name":"名前",
            "skill1":"スキル1",
            "race": "種族",
            "lv":"レベル",
            "picture":"キャラクターイメージ",
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'