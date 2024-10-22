# Generated by Django 4.2.4 on 2024-01-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0022_organizationkyc_social_media_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationvisithistory',
            name='id_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='organizationvisithistory',
            name='type_of_id',
            field=models.CharField(blank=True, choices=[('License', 'License'), ('Passport', 'Passport'), ('Citizenship', 'Citizenship')], max_length=20, null=True),
        ),
    ]
