# Generated by Django 4.1.3 on 2022-12-29 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0002_user_password_alter_user_confirmed'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='adoptioncenter',
            table='"adoption_center"',
        ),
        migrations.AlterModelTable(
            name='adoptionorder',
            table='"adoption_order"',
        ),
        migrations.AlterModelTable(
            name='pet',
            table='pet',
        ),
        migrations.AlterModelTable(
            name='petstore',
            table='"pet_store"',
        ),
        migrations.AlterModelTable(
            name='petstorepurchaseorder',
            table='"pet_store_purchase_order"',
        ),
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
        migrations.AlterModelTable(
            name='postcomment',
            table='"post_comment"',
        ),
        migrations.AlterModelTable(
            name='postreaction',
            table='"post_reaction"',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
