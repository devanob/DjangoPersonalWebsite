# Generated by Django 2.2.1 on 2019-07-02 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectUser', '0003_auto_20190313_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
