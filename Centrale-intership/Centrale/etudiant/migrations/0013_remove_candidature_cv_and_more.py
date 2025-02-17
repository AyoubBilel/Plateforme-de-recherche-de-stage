# Generated by Django 5.0.6 on 2024-06-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0012_offre_de_stage_ce_que_nous_offrons_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidature',
            name='CV',
        ),
        migrations.RemoveField(
            model_name='candidature',
            name='Lettre de motivation',
        ),
        migrations.AddField(
            model_name='candidature',
            name='lettre',
            field=models.FileField(default=None, upload_to='lettres/'),
        ),
        migrations.AddField(
            model_name='candidature',
            name='cv',
            field=models.FileField(default=None, upload_to='cvs/'),
        ),
    ]
