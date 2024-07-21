# Generated by Django 5.0.6 on 2024-07-20 20:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("whatisfordinner", "0002_member_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="email",
            field=models.EmailField(
                max_length=254,
                unique=True,
                validators=[django.core.validators.EmailValidator()],
            ),
        ),
    ]
