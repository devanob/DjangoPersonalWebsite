# Generated by Django 2.1.7 on 2019-02-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, unique=True)),
                ('slug', models.SlugField(help_text='A label for URL config.', max_length=31, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]