# Generated by Django 2.2.7 on 2019-11-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo_url', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('care_tips', models.TextField()),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
