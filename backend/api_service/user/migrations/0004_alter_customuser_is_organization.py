# Generated by Django 4.2.4 on 2024-01-01 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_organization',
            field=models.BooleanField(default=True),
        ),
    ]