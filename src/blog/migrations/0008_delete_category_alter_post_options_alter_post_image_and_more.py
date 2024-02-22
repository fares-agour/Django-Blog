# Generated by Django 4.1.13 on 2024-02-22 17:21

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_remove_post_categories"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Category",
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["created"]},
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to=blog.models.img_upload),
        ),
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("DF", "Draft"), ("CR", "Created")], default="DF", max_length=2
            ),
        ),
    ]