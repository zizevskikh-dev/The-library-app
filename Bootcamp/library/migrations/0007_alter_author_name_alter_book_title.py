# Generated by Django 5.0.7 on 2024-08-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_author_name_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(unique=True),
        ),
    ]
