# Generated by Django 3.0.6 on 2021-05-18 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210514_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status1',
            field=models.BooleanField(default=False),
        ),
    ]
