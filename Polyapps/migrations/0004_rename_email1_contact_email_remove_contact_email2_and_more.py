# Generated by Django 4.0.3 on 2023-02-23 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Polyapps', '0003_alter_contact_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email1',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email2',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='location',
        ),
    ]
