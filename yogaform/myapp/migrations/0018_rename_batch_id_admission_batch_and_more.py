# Generated by Django 4.1.4 on 2022-12-12 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_rename_batch_admission_batch_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission',
            old_name='batch_id',
            new_name='batch',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='batch_id',
            new_name='batch',
        ),
    ]
