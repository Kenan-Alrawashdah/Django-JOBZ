# Generated by Django 4.0.5 on 2022-07-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0003_jop_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
