# Generated by Django 4.1.3 on 2022-11-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('order_name', models.CharField(max_length=100)),
                ('order_phone', models.CharField(max_length=50)),
            ],
        ),
    ]
