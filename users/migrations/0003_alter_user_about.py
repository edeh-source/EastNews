# Generated by Django 5.0.4 on 2024-05-20 09:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
