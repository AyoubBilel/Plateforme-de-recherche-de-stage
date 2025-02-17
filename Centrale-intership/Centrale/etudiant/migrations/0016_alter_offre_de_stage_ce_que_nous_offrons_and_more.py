# Generated by Django 5.0.6 on 2024-06-15 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0015_rename_s_users_service_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre_de_stage',
            name='Ce_que_nous_offrons',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offre_de_stage',
            name='Missions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offre_de_stage',
            name='Profil_recherché',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offre_de_stage',
            name='secteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='etudiant.secteur'),
        ),
    ]
