# Generated by Django 2.1.7 on 2019-03-31 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20190331_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, upload_to='img/project_img/'),
        ),
    ]
