# Generated by Django 5.0.3 on 2024-04-05 13:25

import Registration.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=Registration.models.code_generator, max_length=5)),
            ],
        ),
    ]
