# Generated by Django 4.1.4 on 2022-12-12 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='batch_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.batch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admission',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='batch',
            name='time',
            field=models.CharField(choices=[('M1', '6-7 AM'), ('M2', '7-8 AM'), ('M3', '8-9 AM'), ('E', '5-6 PM')], default=True, max_length=20),
        ),
    ]
