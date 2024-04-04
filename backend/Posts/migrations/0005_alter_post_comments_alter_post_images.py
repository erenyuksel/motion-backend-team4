# Generated by Django 5.0.3 on 2024-04-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_alter_post_options_remove_post_shared_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='post_comments', to='Posts.comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='post_images', to='Posts.image'),
        ),
    ]
