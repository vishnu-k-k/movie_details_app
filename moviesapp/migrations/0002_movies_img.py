# Generated by Django 4.1.6 on 2023-03-04 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default=1, upload_to='movie_pics'),
            preserve_default=False,
        ),
    ]
