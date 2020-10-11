# Generated by Django 3.1.2 on 2020-10-11 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('fullname', models.CharField(max_length=40, verbose_name='Name')),
                ('address', models.TextField(blank=True, verbose_name='Address')),
                ('user_type', models.CharField(blank=True, choices=[('CU', 'Customer'), ('ST', 'Staff')], default='CU', max_length=2, verbose_name='User Type')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.Unselect this instead of deleting accounts.', verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Custom user',
                'verbose_name_plural': 'Custom users',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('U', 'Unassigned'), ('A', 'Assigned'), ('P', 'Picked Up'), ('D', 'Delivered')], default='U', max_length=1, verbose_name='Status')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('B', 'Busy'), ('A', 'Available')], default='A', max_length=1, verbose_name='User Type')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courier.package')),
            ],
        ),
    ]
