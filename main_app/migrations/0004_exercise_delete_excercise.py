# Generated by Django 4.0.6 on 2022-07-09 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_artist_excercise_workout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('reps', models.IntegerField(default=0)),
                ('sets', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='main_app.workout')),
            ],
        ),
        migrations.DeleteModel(
            name='Excercise',
        ),
    ]
