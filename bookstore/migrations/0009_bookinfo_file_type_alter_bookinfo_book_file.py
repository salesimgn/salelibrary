# Generated by Django 4.2.5 on 2023-10-01 20:34

import bookstore.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0008_bookinfo_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='file_type',
            field=models.CharField(choices=[('pdf', 'pdf'), ('docx', 'docx'), ('ppt', 'ppt')], default='pdf', max_length=255),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='book_file',
            field=models.FileField(max_length=255, null=True, upload_to=bookstore.models.set_pdf_filename, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'docx'])]),
        ),
    ]