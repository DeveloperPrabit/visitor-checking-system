# Generated by Django 4.2.4 on 2024-01-16 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_remove_customuser_id_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleOfUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('sub_admin', 'Sub Admin'), ('account', 'Account'), ('editor', 'Editor')], max_length=20)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='org_acc_roles', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_acc_roles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Role of User',
                'verbose_name_plural': 'Roles of Users',
            },
        ),
    ]