# Generated by Django 3.1.6 on 2021-03-03 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('friend', 'Friend request'), ('like', 'Like'), ('message', 'Message'), ('mention', 'Mention')], max_length=20),
        ),
    ]
