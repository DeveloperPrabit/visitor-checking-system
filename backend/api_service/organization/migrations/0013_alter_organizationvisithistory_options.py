# Generated by Django 4.2.4 on 2023-12-31 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0012_remove_organizationbranch_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationvisithistory',
            options={'verbose_name': 'History', 'verbose_name_plural': 'Histories'},
        ),
    ]
