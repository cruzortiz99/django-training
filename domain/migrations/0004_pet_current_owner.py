# Generated by Django 4.1.3 on 2022-12-29 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0003_alter_adoptioncenter_table_alter_adoptionorder_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='current_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='domain.user'),
        ),
    ]