# Generated by Django 3.0.5 on 2020-04-16 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20200416_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliancestatus',
            name='email_add',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
