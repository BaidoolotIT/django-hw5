# Generated by Django 4.1.1 on 2022-09-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiile', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
