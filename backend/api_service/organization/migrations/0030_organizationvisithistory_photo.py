# Generated by Django 4.2.4 on 2024-01-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0029_device_ip_address_alter_device_device_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationvisithistory',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='visitors/%Y/%m/%d/'),
        ),
    ]