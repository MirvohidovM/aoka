# Generated by Django 3.2.13 on 2022-08-02 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpendataAttachments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('title', models.CharField(max_length=512, verbose_name='Mavzusi')),
                ('title_uz', models.CharField(max_length=512, null=True, verbose_name='Mavzusi')),
                ('title_uzb', models.CharField(max_length=512, null=True, verbose_name='Mavzusi')),
                ('title_ru', models.CharField(max_length=512, null=True, verbose_name='Mavzusi')),
                ('title_en', models.CharField(max_length=512, null=True, verbose_name='Mavzusi')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opendata_opendataattachments_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opendata_opendataattachments_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "Qo'shimcha ma'lumot",
                'verbose_name_plural': "Qo'shimcha ma'lumotlar",
                'db_table': 'opendata_attachments',
            },
        ),
        migrations.CreateModel(
            name='OpendataAttachmentsFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='Nomi')),
                ('name_uzb', models.CharField(max_length=255, null=True, verbose_name='Nomi')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Nomi')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Nomi')),
                ('file', models.FileField(upload_to='files/OpendataAttachments')),
                ('opendata_attachments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='opendata.opendataattachments', verbose_name='Fayllar')),
            ],
            options={
                'verbose_name': "Ochiq ma'lumot fayllari",
                'verbose_name_plural': "Ochiq ma'lumotlar fayllari",
                'db_table': 'opendata_attachments_files',
            },
        ),
        migrations.CreateModel(
            name='Opendata',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('title', models.CharField(max_length=500, verbose_name='Sarlavha')),
                ('title_uz', models.CharField(max_length=500, null=True, verbose_name='Sarlavha')),
                ('title_uzb', models.CharField(max_length=500, null=True, verbose_name='Sarlavha')),
                ('title_ru', models.CharField(max_length=500, null=True, verbose_name='Sarlavha')),
                ('title_en', models.CharField(max_length=500, null=True, verbose_name='Sarlavha')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('link', models.URLField(blank=True, max_length=500, null=True, verbose_name='Havola')),
                ('xml_link', models.CharField(max_length=256)),
                ('csv_link', models.CharField(max_length=256)),
                ('json_link', models.CharField(max_length=256)),
                ('xls_link', models.CharField(max_length=256)),
                ('rdf_link', models.CharField(max_length=256)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opendata_opendata_created_by', to=settings.AUTH_USER_MODEL)),
                ('menu', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opendata', to='menu.menu', verbose_name='Menyu')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opendata_opendata_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "Ochiq ma'lumot",
                'verbose_name_plural': "Ochiq ma'lumotlar",
                'db_table': 'open_data',
                'ordering': ('index',),
            },
        ),
    ]