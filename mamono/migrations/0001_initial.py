# Generated by Django 4.0.1 on 2022-01-07 16:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkillModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=20)),
                ('skill_attack', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StatusModels',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('HP', models.IntegerField()),
                ('MP', models.IntegerField()),
                ('ID', models.UUIDField(default=uuid.UUID('aa8ea0e3-4f5c-4bce-88ee-2f85c1bb0fa1'), editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MonsterModels',
            fields=[
                ('statusmodels_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mamono.statusmodels')),
                ('skill1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mamono.skillmodels')),
            ],
            bases=('mamono.statusmodels',),
        ),
    ]
