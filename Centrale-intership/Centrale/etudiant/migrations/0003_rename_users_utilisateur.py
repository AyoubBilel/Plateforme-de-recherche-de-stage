# Generated by Django 5.0.4 on 2024-04-21 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0002_rename_name_users_first_name_users_last_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='utilisateur',
        ),
    ]
