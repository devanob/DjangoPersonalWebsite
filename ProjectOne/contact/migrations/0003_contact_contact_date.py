# Generated by Django 2.1.7 on 2019-04-09 21:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20190407_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
