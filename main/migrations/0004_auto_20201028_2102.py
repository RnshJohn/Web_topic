# Generated by Django 3.1.2 on 2020-10-28 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201028_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='mainimage',
            new_name='image',
        ),
    ]