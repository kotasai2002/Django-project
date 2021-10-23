# Generated by Django 3.0.6 on 2021-05-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_product_status1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=20)),
                ('state', models.CharField(max_length=40)),
                ('subject', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'queries',
            },
        ),
    ]
