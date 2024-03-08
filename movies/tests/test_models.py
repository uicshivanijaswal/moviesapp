from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModels:
    def test_movie_is_post_production_completed(self):
        movie = mixer.blend('movies.Movie', duration=120)
        assert movie.is_post_production_completed == True