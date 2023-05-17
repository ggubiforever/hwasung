# Generated by Django 4.2 on 2023-04-21 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bom_mng", "0003_alter_bom1_last_update_alter_bom2_last_update"),
    ]

    operations = [
        migrations.AddField(
            model_name="bom1",
            name="editor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="bom1",
            name="man_edit_yn",
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name="bom1",
            name="man_edt_modifydate",
            field=models.DateTimeField(null=True),
        ),
    ]
