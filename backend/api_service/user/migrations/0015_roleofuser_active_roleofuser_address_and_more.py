# Generated by Django 4.2.4 on 2024-01-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_roleofuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='roleofuser',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='roleofuser',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='roleofuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='roleofuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='roleofuser',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='roleofuser',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='roleofuser',
            name='role',
            field=models.CharField(blank=True, choices=[('admin', 'Admin'), ('sub_admin', 'Sub Admin'), ('account', 'Account'), ('editor', 'Editor')], max_length=20, null=True),
        ),
    ]
