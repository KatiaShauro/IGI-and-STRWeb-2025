# Generated by Django 5.2.1 on 2025-05-17 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_manager', '0005_alter_vacancy_options_contacts_work_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='image',
        ),
    ]
