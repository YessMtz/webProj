# Generated by Django 5.0.9 on 2024-11-13 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=32)),
                ('apellido', models.CharField(max_length=32)),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
    ]