# Generated by Django 4.0.6 on 2022-07-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmsapp', '0003_movie_img_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='desc',
            field=models.TextField(max_length=156),
        ),
    ]
