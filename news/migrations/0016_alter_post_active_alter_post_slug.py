# Generated by Django 5.0.4 on 2024-05-26 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_post_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=256, unique_for_date='publish'),
        ),
    ]
