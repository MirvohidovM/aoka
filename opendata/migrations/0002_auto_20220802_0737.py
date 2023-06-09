# Generated by Django 3.2.13 on 2022-08-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opendata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opendata',
            name='csv_link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='CSV havolasi'),
        ),
        migrations.AlterField(
            model_name='opendata',
            name='json_link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='JSON havolasi'),
        ),
        migrations.AlterField(
            model_name='opendata',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Asosiy Havola'),
        ),
        migrations.AlterField(
            model_name='opendata',
            name='rdf_link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='RDF havolasi'),
        ),
        migrations.AlterField(
            model_name='opendata',
            name='xls_link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='XLS havolasi'),
        ),
        migrations.AlterField(
            model_name='opendata',
            name='xml_link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='XML havolasi'),
        ),
    ]
