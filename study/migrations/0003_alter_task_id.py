# Generated by Django 3.2.13 on 2022-05-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_remove_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
