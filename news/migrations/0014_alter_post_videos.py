# Generated by Django 5.0.4 on 2024-05-23 19:16

import embed_video.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_message_alter_comment_options_alter_reply_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='videos',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]
