# Generated by Django 4.2.8 on 2023-12-11 12:55

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0049_alter_remoterealmbillinguser_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="preregistrationremoterealmbillinguser",
            name="created_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="zilencer.remoterealmbillinguser",
            ),
        ),
        migrations.AddField(
            model_name="preregistrationremoterealmbillinguser",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="preregistrationremoteserverbillinguser",
            name="created_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="zilencer.remoteserverbillinguser",
            ),
        ),
        migrations.AddField(
            model_name="preregistrationremoteserverbillinguser",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="remoterealmbillinguser",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="remoterealmbillinguser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="remoterealmbillinguser",
            name="last_login",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="remoteserverbillinguser",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="remoteserverbillinguser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="remoteserverbillinguser",
            name="last_login",
            field=models.DateTimeField(null=True),
        ),
    ]