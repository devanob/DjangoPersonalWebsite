# Generated by Django 2.1.7 on 2019-02-19 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20190219_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
