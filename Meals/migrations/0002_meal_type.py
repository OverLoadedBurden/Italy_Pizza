# Generated by Django 2.2.5 on 2020-02-15 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Meals.Types'),
            preserve_default=False,
        ),
    ]