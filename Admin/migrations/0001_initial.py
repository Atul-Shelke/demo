# Generated by Django 4.1.4 on 2023-03-28 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades', models.CharField(max_length=100)),
                ('isactive', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Grades',
            },
        ),
    ]
