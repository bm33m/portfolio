# Generated by Django 3.0.5 on 2023-05-08 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_number', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('log_type', models.CharField(default='Signup', max_length=256)),
                ('user_type', models.CharField(default='Other', max_length=30)),
                ('notes', models.TextField(blank=True)),
                ('date_login', models.DateTimeField(blank=True)),
                ('date_logout', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_number', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('usertype', models.CharField(default='Other', max_length=30)),
                ('usertypesa', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=64)),
                ('location', models.TextField(blank=True)),
                ('longitude', models.CharField(blank=True, max_length=128)),
                ('latitude', models.CharField(blank=True, max_length=128)),
                ('address', models.TextField(blank=True)),
                ('street', models.CharField(blank=True, max_length=128)),
                ('town', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(blank=True, max_length=128)),
                ('province', models.CharField(blank=True, max_length=128)),
                ('code', models.CharField(blank=True, max_length=32)),
                ('country', models.CharField(blank=True, max_length=128)),
                ('address_type', models.CharField(default='home', max_length=30)),
                ('notes', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(blank=True)),
                ('date_modified', models.DateTimeField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]