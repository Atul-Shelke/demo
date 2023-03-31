# Generated by Django 4.1.4 on 2023-03-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='schoolregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.BigIntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]