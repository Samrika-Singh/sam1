# Generated by Django 3.0.2 on 2020-02-08 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20200123_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comments_count',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='upvotes',
        ),
    ]