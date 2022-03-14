# Generated by Django 3.2 on 2021-06-15 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipments', '0004_alter_shipments_cellphone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipments',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipments', to='auth.user'),
            preserve_default=False,
        ),
    ]