# Generated by Django 2.1.7 on 2019-03-14 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_project_projecthandlier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='project_tag', to='organizer.Tag'),
        ),
    ]
