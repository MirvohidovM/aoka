# Generated by Django 3.2.13 on 2022-07-15 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PressSecretary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name="To'liq ismi")),
                ('biography', models.TextField(verbose_name='Biografiyasi')),
                ('phone', models.CharField(max_length=30, verbose_name='Telefon raqami')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Matbuot kotibi',
                'verbose_name_plural': 'Matbuot kotibi',
                'db_table': 'press_secretary',
            },
        ),
    ]