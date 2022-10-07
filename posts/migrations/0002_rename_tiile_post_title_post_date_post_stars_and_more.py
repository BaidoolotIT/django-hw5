# Generated by Django 4.1.1 on 2022-09-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tiile',
            new_name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='stars',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(1, 'animals'), (2, 'car'), (3, 'tir'), (3, 'other')], null=True),
        ),
    ]
