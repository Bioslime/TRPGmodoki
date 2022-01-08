from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


# Create your models here.


class StatusModels(models.Model):
    name = models.CharField(max_length=20, unique=True)
    picture = models.ImageField(default="defo", upload_to='char_image/')
    HP = models.PositiveBigIntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(1000)])
    MP = models.PositiveBigIntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(1000)])
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    def __str__(self):
        return self.name


class SkillModels(models.Model):
    skill_name = models.CharField(max_length=20, unique=True)
    skill_attack = models.PositiveBigIntegerField(default=1, validators=[MinValueValidator(0)])
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.skill_name


class MonsterModels(StatusModels):
    skill1 = models.ForeignKey(SkillModels, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name


class RaceModels(models.Model):
    race_name = models.CharField(max_length=20, unique=True)
    race_skill = models.ForeignKey(SkillModels, on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.race_name


class YushaModels(StatusModels):
    skill1 = models.ForeignKey(SkillModels, on_delete=models.SET_NULL, null=True)
    lv = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(100)])
    race = models.ForeignKey(RaceModels, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name



