# Generated by Django 3.0.8 on 2020-08-16 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200816_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapstore',
            name='community',
        ),
        migrations.RemoveField(
            model_name='mapstore',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='mapstore',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='mapstore',
            name='user',
        ),
        migrations.DeleteModel(
            name='ListStore',
        ),
        migrations.DeleteModel(
            name='MapStore',
        ),
    ]
