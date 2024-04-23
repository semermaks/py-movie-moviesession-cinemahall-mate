from django.db.models.query import QuerySet

from db.models import Movie, Actor, Genre


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    movies = Movie.objects.all()
    if genres_ids is not None and actors_ids is not None:
        movies = movies.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct()
    elif genres_ids is not None:
        movies = movies.filter(genres__id__in=genres_ids).distinct()
    elif actors_ids is not None:
        movies = movies.filter(actors__id__in=actors_ids).distinct()
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: int = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(Genre.objects.filter(id__in=genres_ids))
    if actors_ids:
        movie.actors.set(Actor.objects.filter(id__in=actors_ids))
    return movie
