# Generated by Django 4.2.4 on 2023-12-23 06:19

from django.db import migrations, models
import organization.models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_alter_organizationkyc_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationdocument',
            name='file',
            field=models.FileField(upload_to=organization.models.upload_to_organization_document),
        ),
    ]