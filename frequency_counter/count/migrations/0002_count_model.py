# Generated by Django 3.2.3 on 2021-05-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='count_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('count', models.CharField(max_length=100)),
            ],
        ),
    ]
