from django.test import TestCase
import pytest
from django.urls import reverse

_test_case = TestCase()

assert_contains = _test_case.assertContains
assert_not_contains = _test_case.assertNotContains
assert_template = _test_case.assertTemplateUsed

# class HomeTest(TestCase):
#     """
#     Test home
#     """

#     def setUp(self):
#         self.response = self.client.get('/')

#     def test_get(self):
#         """GET / must return status code 200"""
#         self.assertEqual(200, self.response.status_code)

#     def test_template(self):
#         """Must use core/home.html"""
#         self.assertTemplateUsed(self.response, 'core/home.html')

#     def test_html(self):
#         """HTML must contain"""
#         self.assertContains(self.response, 'Francisco Bustamante')
#         self.assertContains(self.response, 'Python developer')
#         self.assertContains(self.response, '<article', 8)


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_template(resp):
    assert_template(resp, 'core/home.html')


def test_html(resp):
    """HTML must contain"""
    assert_contains(resp, 'Francisco Bustamante')
    assert_contains(resp, 'Python developer')
    assert_contains(resp, '<article', 8)
