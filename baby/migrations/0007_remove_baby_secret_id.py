# Generated by Django 3.1.4 on 2021-06-14 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baby', '0006_baby_announce_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baby',
            name='secret_id',
        ),
    ]
