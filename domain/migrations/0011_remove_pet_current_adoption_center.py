# Generated by Django 4.1.3 on 2022-12-31 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0010_rename_user_account_alter_account_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='current_adoption_center',
        ),
    ]
