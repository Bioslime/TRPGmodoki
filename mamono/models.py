from django.db import models
from django.db.models.deletion import CASCADE
import uuid

# Create your models here.


class StatusModels(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField(default="defo", upload_to='char_image/')
    HP = models.IntegerField()
    MP = models.IntegerField()
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    def __str__(self):
        return self.name


class SkillModels(models.Model):
    skill_name = models.CharField(max_length=20)
    skill_attack = models.IntegerField()
    def __str__(self):
        return self.skill_name


class MonsterModels(StatusModels):
    skill1 = models.ForeignKey(SkillModels, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
