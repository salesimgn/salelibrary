# Generated by Django 4.2.5 on 2023-09-23 16:45

import bookstore.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstore', '0003_alter_book_info_book_file_alter_book_info_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_info',
            name='book_file',
        ),
        migrations.RemoveField(
            model_name='book_info',
            name='cover',
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('author', models.CharField(max_length=255, null=True)),
                ('Pages', models.IntegerField()),
                ('size', models.CharField(max_length=50)),
                ('published_year', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(max_length=255)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=bookstore.models.set_cover_filename)),
                ('book_file', models.FileField(max_length=255, null=True, upload_to=bookstore.models.set_pdf_filename, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('upload_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]