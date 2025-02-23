# Generated by Django 4.2.4 on 2023-10-10 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('municipality', models.CharField(max_length=100)),
                ('city_village_area', models.CharField(max_length=100)),
                ('ward_no', models.CharField(max_length=10)),
                ('employee_size', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='documents/None/')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationKYC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('establishment_year', models.PositiveIntegerField()),
                ('vat_number', models.CharField(max_length=50)),
                ('pan_number', models.CharField(max_length=50)),
                ('registration_number', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('municipality', models.CharField(max_length=100)),
                ('city_village_area', models.CharField(blank=True, max_length=100, null=True)),
                ('ward_no', models.CharField(max_length=10)),
                ('organization_summary', models.TextField()),
                ('whatsapp_viber_number', models.CharField(max_length=20)),
                ('secondary_number', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationSocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationVisitHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=50, null=True)),
                ('purpose', models.CharField(max_length=250)),
                ('have_vehicle', models.BooleanField(blank=True, default=False, null=True)),
                ('vehicle_number', models.CharField(blank=True, max_length=50, null=True)),
                ('is_with_team', models.BooleanField(blank=True, default=False, null=True)),
                ('number_of_team', models.IntegerField(blank=True, default=0, null=True)),
                ('visiting_from', models.CharField(max_length=250)),
                ('is_approved', models.BooleanField(default=False)),
                ('visited_at', models.DateTimeField(auto_now_add=True)),
                ('departed_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
