# Generated by Django 3.1.6 on 2021-03-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210303_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
