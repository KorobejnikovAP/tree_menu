# Generated by Django 5.0 on 2023-12-11 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menu'),
        ),
    ]
