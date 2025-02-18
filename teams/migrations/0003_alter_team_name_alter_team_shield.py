# Generated by Django 5.1.6 on 2025-02-15 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_remove_team_image_team_shield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='shield',
            field=models.ImageField(blank=True, default='teams/shields/default.png', null=True, upload_to='teams/shields'),
        ),
    ]
