# Generated by Django 5.1.7 on 2025-03-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('exp', models.IntegerField()),
            ],
        ),
    ]
