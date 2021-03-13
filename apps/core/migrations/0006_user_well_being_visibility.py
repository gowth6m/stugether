# Generated by Django 3.1.6 on 2021-03-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_topic_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='well_being_visibility',
            field=models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('show_friends', 'Show friends')], default='private', max_length=20),
        ),
    ]
