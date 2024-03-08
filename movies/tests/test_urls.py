from django.urls import reverse, resolve

class TestUrls:
    def test_detail_url(self):
        path = reverse('movies:index', kwargs={})
        assert resolve(path).view_name == 'movies:index'