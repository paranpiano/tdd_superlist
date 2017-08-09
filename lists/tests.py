from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page #1

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  # find root page with resolve function
        print(found)
        self.assertEqual(found.func, home_page)