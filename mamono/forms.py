from django import forms
from django.db.models import fields
from .models import MonsterModels, SkillModels


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