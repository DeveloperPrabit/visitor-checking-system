# Generated by Django 4.2.4 on 2024-02-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0041_alter_organizationvisithistory_visiting_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationkyc',
            name='accept',
        ),
        migrations.AddField(
            model_name='organizationkyc',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]
