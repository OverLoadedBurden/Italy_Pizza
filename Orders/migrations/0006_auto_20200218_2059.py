# Generated by Django 2.2.5 on 2020-02-18 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0005_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
