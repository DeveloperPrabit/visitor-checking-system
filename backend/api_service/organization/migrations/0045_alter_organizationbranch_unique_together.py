# Generated by Django 4.2.4 on 2024-02-12 15:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0044_organizationbranch_qr_image_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='organizationbranch',
            unique_together={('organization', 'branch_no')},
        ),
    ]
