# Generated by Django 4.2.4 on 2024-01-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0025_organizationvisithistory_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationbranch',
            name='branch_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='organizationbranch',
            name='contact_person',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='organizationbranch',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organizationbranch',
            name='city_village_area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='organizationbranch',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='organizationbranch',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='organizationbranch',
            name='employee_size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='organizationbranch',
            name='municipality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='organizationbranch',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organizationbranch',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='organizationbranch',
            name='ward_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]