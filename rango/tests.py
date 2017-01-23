from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders

class GeneralTests(TestCase):
  def test_serving_static_files(self):
    result = finders.find('images/rango.jpeg')
    self.assertIsNotNone(result)

class IndexPageTests(TestCase):

    def test_index_contains_hello_message(self):

        response = self.client.get(reverse('index'))
        self.assertIn(b'Rango says', response.content)

    def test_index_using_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'rango/index.html')

    def test_rango_picture_displayed(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'img src="/static/images/rango.jpeg"', response.content)

    def test_index_has_title(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


class AboutPageTests(TestCase):
    def test_about_contains_create_message(self):

        response = self.client.get(reverse('about'))
        self.assertIn(b'This tutorial has been put together by', response.content)

    def test_about_using_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'rango/about.html')

class ModelTests(TestCase):
    def setUp(self):
        from populate_rango import populate
        try:
            populate()
        except ImportError:
            print("This module populate_rango does not exist")
        except NameError:
            print("The function populate() does not exist or is not correct")
        except:
            print("Something went wrong in the populate() function :-(")

    def  get_category(self, name):

        from rango.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None 
        return cat

    def test_python_cat_added(self):
        cat = self.get_category('Python')
        self.assertIsNotNone(cat)

    def test_python_cat_with_views(self):
        cat = self.get_category("Python")
        self.assertEquals(cat.views, 128)

    def test_admin_interface_page_view(self):
        from admin import PageAdmin
        self.assertIn('category', PageAdmin.list_display)
        self.assertIn('url', PageAdmin.list_display)




