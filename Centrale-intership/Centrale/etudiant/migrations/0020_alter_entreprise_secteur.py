# Generated by Django 5.0.6 on 2024-06-16 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0019_remove_alumnis_emploi_remove_alumnis_stage_1a_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreprise',
            name='secteur',
            field=models.CharField(default='*', max_length=255),
        ),
    ]
