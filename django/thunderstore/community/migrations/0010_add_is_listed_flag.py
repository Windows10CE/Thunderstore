# Generated by Django 3.1.6 on 2021-02-25 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0009_add_dynamic_social_auth_settings"),
    ]

    operations = [
        migrations.AddField(
            model_name="community",
            name="is_listed",
            field=models.BooleanField(default=True),
        ),
    ]
