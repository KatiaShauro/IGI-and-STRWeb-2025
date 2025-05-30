# Generated by Django 5.2.1 on 2025-05-19 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_agency', '0010_alter_owner_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, help_text='Статистический график', null=True, upload_to='statistics/', verbose_name='Graphics')),
                ('name', models.CharField()),
                ('main_number', models.FloatField(default=0)),
                ('number2', models.FloatField(default=0, null=True)),
                ('number3', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='deal',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deal_employee', to='estate_agency.employee'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='deal_customer', to='estate_agency.customer'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='realty',
            field=models.ForeignKey(help_text='Объект недвижимости', on_delete=django.db.models.deletion.PROTECT, related_name='deal_realty', to='estate_agency.realty'),
        ),
    ]
