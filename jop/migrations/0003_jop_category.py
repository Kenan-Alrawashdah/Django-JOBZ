# Generated by Django 4.0.5 on 2022-07-02 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jop.category'),
            preserve_default=False,
        ),
    ]
