# Generated by Django 4.0.5 on 2022-07-30 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jop', '0006_alter_apply_cover_letter_alter_apply_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='jop_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
