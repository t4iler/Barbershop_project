# Generated by Django 4.1.3 on 2022-11-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс'),
        ),
    ]
