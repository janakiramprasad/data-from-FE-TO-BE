# Generated by Django 4.2.6 on 2023-12-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jsp',
            fields=[
                ('Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('phno', models.IntegerField()),
            ],
        ),
    ]
