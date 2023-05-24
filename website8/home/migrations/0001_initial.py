# Generated by Django 4.1.7 on 2023-05-10 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='svModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mssv', models.CharField(max_length=10)),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('lop', models.CharField(choices=[('PM01', 'Pm01.'), ('PM02', 'Pm02.'), ('IOT', 'IoT.')], max_length=5)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
