# Generated by Django 3.2.23 on 2024-01-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20240125_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.TextField(choices=[('1', 'Table with view'), ('2', 'Table around ice-fountain'), ('3', 'Big table with lake view'), ('4', 'Big table upstairs with lake view')], default='exit', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TextField(choices=[('3-5', '3pm-5pm'), ('5-7', '5pm-7pm'), ('7-9', '7pm-9pm')], max_length=255),
        ),
    ]
