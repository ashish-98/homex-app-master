# Generated by Django 3.0.4 on 2020-03-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200310_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliancestatus',
            name='status',
            field=models.CharField(choices=[('OFF', 'OFF'), ('ON', 'ON')], max_length=3),
        ),
    ]
