# Generated by Django 4.2.2 on 2023-06-19 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('c_no', models.IntegerField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('ca_no', models.IntegerField(primary_key=True, serialize=False)),
                ('c_capital', models.CharField(max_length=100)),
                ('c_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]
