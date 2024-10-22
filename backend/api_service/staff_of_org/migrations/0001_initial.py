# Generated by Django 4.2.4 on 2024-01-17 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True)),
                ('role', models.CharField(blank=True, choices=[('admin', 'Admin'), ('sub_admin', 'Sub Admin'), ('account', 'Account'), ('editor', 'Editor')], max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='staff_user_groups', related_query_name='group', to='auth.group')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_acc_roles', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='staff_user_user_permissions', related_query_name='user_permission', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
