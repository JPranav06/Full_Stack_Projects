# Generated by Django 4.1.6 on 2023-02-11 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('native', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
                ('CGPA', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]
