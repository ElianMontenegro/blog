# Generated by Django 3.1.4 on 2020-12-15 00:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201214_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=100000, verbose_name='contenido'),
        ),
    ]