# Generated by Django 4.0 on 2022-02-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_remove_pagestwo_slug_pages_auto_compile_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='auto_compile_description',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pagestwo',
            name='auto_compile_description',
            field=models.BooleanField(default=True),
        ),
    ]