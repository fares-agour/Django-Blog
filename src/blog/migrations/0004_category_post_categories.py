# Generated by Django 4.1.13 on 2024-02-16 23:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_post_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(to="blog.category"),
        ),
    ]
