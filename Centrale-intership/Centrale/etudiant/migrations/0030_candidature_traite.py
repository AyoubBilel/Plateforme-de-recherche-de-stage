# Generated by Django 5.0.6 on 2024-06-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0029_offre_de_stage_stage_valide'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidature',
            name='traite',
            field=models.CharField(choices=[('traité', 'traité'), ('non traité', 'non traité')], default='non traité', max_length=20),
        ),
    ]
