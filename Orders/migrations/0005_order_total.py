# Generated by Django 2.2.5 on 2020-02-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0004_auto_20200218_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]