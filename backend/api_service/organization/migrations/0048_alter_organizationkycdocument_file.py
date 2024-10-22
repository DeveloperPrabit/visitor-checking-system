# Generated by Django 4.2.4 on 2024-02-16 03:48

import common.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0047_organizationkycdocument_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationkycdocument',
            name='file',
            field=models.FileField(upload_to='organization_kyc/documents/%Y/%m/%d/', validators=[common.utils.validate_file_size]),
        ),
    ]
