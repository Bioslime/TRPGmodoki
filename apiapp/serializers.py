from rest_framework import serializers
from .models import SkillModels


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillModels
        fields = ('skill_name', 'skill_attack', 'id', )



