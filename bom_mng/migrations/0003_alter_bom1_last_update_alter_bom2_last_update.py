# Generated by Django 4.2 on 2023-04-20 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bom_mng', '0002_bom_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bom1',
            name='last_update',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bom2',
            name='last_update',
            field=models.CharField(max_length=20),
        ),
    ]