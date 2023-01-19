# Generated by Django 4.1.5 on 2023-01-19 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_auth_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_type',
            field=models.CharField(choices=[('via_email', 'via_email'), ('via_phone', 'via_phone'), ('via_username', 'via_username')], default='via_username', max_length=31),
        ),
        migrations.AlterField(
            model_name='userconfirmation',
            name='verify_type',
            field=models.CharField(choices=[('via_phone', 'via_phone'), ('via_email', 'via_email')], max_length=31),
        ),
    ]
