# Generated by Django 4.1.13 on 2024-02-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_delete_category_alter_post_options_alter_post_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("draft", "Draft"), ("created", "Created")],
                default="DF",
                max_length=20,
            ),
        ),
    ]
