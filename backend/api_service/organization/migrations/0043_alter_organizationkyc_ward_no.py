# Generated by Django 4.2.4 on 2024-02-12 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0042_remove_organizationkyc_accept_organizationkyc_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationkyc',
            name='ward_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
