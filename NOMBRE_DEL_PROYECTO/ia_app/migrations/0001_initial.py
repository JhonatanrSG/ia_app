# Generated by Django 4.2.7 on 2023-11-29 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('odbc_driver', models.CharField(max_length=255)),
                ('server', models.CharField(max_length=255)),
                ('database', models.CharField(max_length=255)),
                ('trusted_connection', models.BooleanField(default=True)),
                ('login_timeout', models.IntegerField(default=30)),
                ('encrypt', models.BooleanField(default=False)),
            ],
        ),
    ]
