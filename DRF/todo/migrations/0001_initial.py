# Generated by Django 3.2.8 on 2022-03-27 09:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("link", models.URLField(blank=True, null=True)),
                ("users", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="TODO",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.TextField(blank=True, null=True, verbose_name="текст заметки")),
                ("create_date", models.DateTimeField(auto_now_add=True, verbose_name="дата создания")),
                ("edit_date", models.DateTimeField(auto_now=True, verbose_name="дата обновления")),
                ("active", models.BooleanField()),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="todo.project")),
                (
                    "user_created",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]