# Generated by Django 4.2.5 on 2023-10-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0007_alter_bookinfo_author_alter_bookinfo_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='department',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]