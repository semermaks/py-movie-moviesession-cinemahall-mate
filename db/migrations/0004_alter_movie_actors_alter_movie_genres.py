# Generated by Django 4.0.2 on 2024-05-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_movie_actors_alter_moviesession_cinema_hall_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movie_actors', to='db.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movie_genres', to='db.Genre'),
        ),
    ]