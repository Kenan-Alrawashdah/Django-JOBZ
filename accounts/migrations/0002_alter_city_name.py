# Generated by Django 4.0.5 on 2022-08-01 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
