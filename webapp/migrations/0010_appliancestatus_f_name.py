# Generated by Django 3.0.5 on 2020-04-16 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_appliancestatus_email_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliancestatus',
            name='f_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
